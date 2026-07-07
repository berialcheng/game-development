param(
    [ValidateSet("startup", "script", "capture")]
    [string]$Mode = "startup",
    [string]$ProjectPath = (Resolve-Path ".").Path,
    [string]$GodotExe = $env:GODOT_EXE,
    [string]$ScriptPath = "",
    [int]$TimeoutSeconds = 120,
    [ValidateSet("auto", "true", "false")]
    [string]$Headless = "auto"
)

$ErrorActionPreference = "Stop"
$startedAt = Get-Date
$ProjectPath = (Resolve-Path -LiteralPath $ProjectPath).Path

if ([string]::IsNullOrWhiteSpace($GodotExe)) {
    throw "Set -GodotExe or GODOT_EXE to the Godot console executable path."
}
if (-not (Test-Path -LiteralPath $GodotExe)) {
    throw "Godot executable not found: $GodotExe"
}
if ($Mode -ne "startup" -and [string]::IsNullOrWhiteSpace($ScriptPath)) {
    throw "Mode '$Mode' requires -ScriptPath, for example res://scripts/tools/smoke.gd."
}

function Stop-SameRunWerFault {
    Get-Process WerFault -ErrorAction SilentlyContinue | ForEach-Object {
        $processStart = $null
        try { $processStart = $_.StartTime } catch {}
        if ($processStart -ne $null -and $processStart -ge $startedAt.AddSeconds(-2)) {
            try { Stop-Process -Id $_.Id -Force -ErrorAction Stop } catch {}
        }
    }
}

$logDir = Join-Path $ProjectPath "docs\evidence\generated\godot_logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$runStamp = Get-Date -Format "yyyyMMdd_HHmmss"
$godotLogPath = Join-Path $logDir ("godot_{0}_{1}.log" -f $Mode, $runStamp)
$stdoutPath = Join-Path $logDir ("godot_{0}_{1}.stdout.log" -f $Mode, $runStamp)
$stderrPath = Join-Path $logDir ("godot_{0}_{1}.stderr.log" -f $Mode, $runStamp)

$useHeadless = $false
if ($Headless -eq "true") {
    $useHeadless = $true
} elseif ($Headless -eq "auto") {
    $useHeadless = $Mode -ne "capture"
}

$argsList = New-Object System.Collections.Generic.List[string]
if ($useHeadless) {
    $argsList.Add("--headless")
}
$argsList.Add("--log-file")
$argsList.Add($godotLogPath)
$argsList.Add("--path")
$argsList.Add($ProjectPath)

if ($Mode -eq "startup") {
    $argsList.Add("--quit")
} else {
    $argsList.Add("--script")
    $argsList.Add($ScriptPath)
}

$proc = Start-Process -FilePath $GodotExe -ArgumentList $argsList.ToArray() -PassThru -WindowStyle Hidden -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
$deadline = (Get-Date).AddSeconds($TimeoutSeconds)
while (-not $proc.HasExited -and (Get-Date) -lt $deadline) {
    Start-Sleep -Milliseconds 250
    Stop-SameRunWerFault
}

if (-not $proc.HasExited) {
    try { Stop-Process -Id $proc.Id -Force -ErrorAction Stop } catch {}
    Stop-SameRunWerFault
    throw "Godot $Mode timed out after $TimeoutSeconds seconds. Logs: $godotLogPath, $stdoutPath, $stderrPath"
}

Stop-SameRunWerFault
if ($proc.ExitCode -ne 0) {
    throw "Godot $Mode failed with exit code $($proc.ExitCode). Logs: $godotLogPath, $stdoutPath, $stderrPath"
}

$scanPaths = @($godotLogPath, $stdoutPath, $stderrPath) | Where-Object { Test-Path -LiteralPath $_ }
$errors = @()
foreach ($path in $scanPaths) {
    $matches = Select-String -LiteralPath $path -Pattern "SCRIPT ERROR:", "ERROR:" -SimpleMatch -ErrorAction SilentlyContinue
    if ($matches) {
        $errors += $matches | ForEach-Object { "$($_.Path):$($_.LineNumber): $($_.Line.Trim())" }
    }
}
if ($errors.Count -gt 0) {
    throw "Godot $Mode emitted validation errors:`n$($errors -join "`n")"
}

Write-Output ("Godot {0} passed. Log: {1}" -f $Mode, $godotLogPath)