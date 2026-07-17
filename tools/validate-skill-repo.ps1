param(
    [switch]$CheckInstalled
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$SkillsRoot = Join-Path $RepoRoot "skills"
$QuickValidate = Join-Path $HOME ".codex\skills\.system\skill-creator\scripts\quick_validate.py"
$Errors = [System.Collections.Generic.List[string]]::new()
$Warnings = [System.Collections.Generic.List[string]]::new()

$LineBudgets = @{
    "game-reference-research" = 120
    "synthetic-gameplay-review" = 130
    "synthesize-playtest-feedback" = 130
    "game-production-orchestrator" = 130
    "generate2dmap" = 200
    "generate2dsprite" = 190
    "godot-2d-implementation" = 170
}

function Add-CheckError([string]$Message) {
    $Errors.Add($Message)
    Write-Host "FAIL  $Message" -ForegroundColor Red
}

function Add-CheckWarning([string]$Message) {
    $Warnings.Add($Message)
    Write-Host "WARN  $Message" -ForegroundColor Yellow
}

function Add-CheckPass([string]$Message) {
    Write-Host "PASS  $Message" -ForegroundColor Green
}

function Get-FrontmatterValue([string]$Text, [string]$Name) {
    $pattern = '(?m)^' + [regex]::Escape($Name) + ':\s*"?([^"\r\n]+)"?\s*$'
    return [regex]::Match($Text, $pattern).Groups[1].Value.Trim()
}

Push-Location $RepoRoot
try {
    $SkillDirs = Get-ChildItem $SkillsRoot -Directory | Where-Object {
        Test-Path (Join-Path $_.FullName "SKILL.md")
    } | Sort-Object Name
    $SkillNames = @($SkillDirs.Name)

    if (-not (Test-Path $QuickValidate)) {
        Add-CheckError "quick_validate.py not found at $QuickValidate"
    }
    else {
        foreach ($SkillDir in $SkillDirs) {
            & python $QuickValidate $SkillDir.FullName
            if ($LASTEXITCODE -ne 0) {
                Add-CheckError "$($SkillDir.Name) failed quick_validate.py"
            }
            else {
                Add-CheckPass "$($SkillDir.Name) passed quick_validate.py"
            }
        }
    }

    $Registry = Get-Content -Raw (Join-Path $RepoRoot "skill-repo.json") | ConvertFrom-Json
    $Package = Get-Content -Raw (Join-Path $RepoRoot "package.json") | ConvertFrom-Json
    $RegistryNames = @($Registry.skills.name | Sort-Object)
    $PackageNames = @($Package.skills.paths | ForEach-Object { Split-Path $_ -Leaf } | Sort-Object)

    if ((Compare-Object $SkillNames $RegistryNames | Measure-Object).Count -gt 0) {
        Add-CheckError "skills/ and skill-repo.json expose different skill names"
    }
    else {
        Add-CheckPass "skills/ and skill-repo.json agree"
    }

    if ((Compare-Object $SkillNames $PackageNames | Measure-Object).Count -gt 0) {
        Add-CheckError "skills/ and package.json expose different skill names"
    }
    else {
        Add-CheckPass "skills/ and package.json agree"
    }

    $RootReadme = Get-Content -Raw (Join-Path $RepoRoot "README.md")
    $SkillReadme = Get-Content -Raw (Join-Path $SkillsRoot "README.md")

    foreach ($SkillDir in $SkillDirs) {
        $Name = $SkillDir.Name
        $SkillPath = Join-Path $SkillDir.FullName "SKILL.md"
        $SkillText = Get-Content -Raw $SkillPath
        $Description = Get-FrontmatterValue $SkillText "description"
        $LineCount = (Get-Content $SkillPath).Count
        $Budget = $LineBudgets[$Name]

        if ($LineCount -gt $Budget) {
            Add-CheckError "$Name SKILL.md has $LineCount lines; budget is $Budget"
        }
        else {
            Add-CheckPass "$Name SKILL.md is within its line budget"
        }

        if ($Description.Length -gt 350) {
            Add-CheckError "$Name frontmatter description is $($Description.Length) characters; limit is 350"
        }

        $RegistryEntry = $Registry.skills | Where-Object { $_.name -eq $Name }
        if ($null -eq $RegistryEntry -or $RegistryEntry.description -ne $Description) {
            Add-CheckError "$Name registry description does not match SKILL.md frontmatter"
        }

        if ($RootReadme -notmatch [regex]::Escape($Name)) {
            Add-CheckError "README.md does not mention $Name"
        }
        if ($SkillReadme -notmatch [regex]::Escape($Name)) {
            Add-CheckError "skills/README.md does not mention $Name"
        }

        $OpenAIYaml = Join-Path $SkillDir.FullName "agents\openai.yaml"
        if (-not (Test-Path $OpenAIYaml)) {
            Add-CheckError "$Name has no agents/openai.yaml"
        }
        else {
            $YamlText = Get-Content -Raw $OpenAIYaml
            $Short = [regex]::Match($YamlText, '(?m)^\s*short_description:\s*"([^"]*)"').Groups[1].Value
            $Prompt = [regex]::Match($YamlText, '(?m)^\s*default_prompt:\s*"([^"]*)"').Groups[1].Value
            if ($Short.Length -lt 25 -or $Short.Length -gt 64) {
                Add-CheckError "$Name short_description has $($Short.Length) characters; expected 25-64"
            }
            if ($Prompt.Length -gt 300) {
                Add-CheckError "$Name default_prompt has $($Prompt.Length) characters; limit is 300"
            }
            if ($Prompt -notmatch [regex]::Escape("`$$Name")) {
                Add-CheckError "$Name default_prompt does not mention `$$Name"
            }
        }
    }

    $MarkdownFiles = Get-ChildItem $SkillsRoot -Recurse -File -Filter "*.md"
    foreach ($MarkdownFile in $MarkdownFiles) {
        $Text = Get-Content -Raw $MarkdownFile.FullName
        foreach ($Match in [regex]::Matches($Text, '\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)')) {
            $Link = $Match.Groups[1].Value
            if ($Link -match '^(https?://|mailto:)') {
                continue
            }
            $Target = Join-Path $MarkdownFile.DirectoryName $Link
            if (-not (Test-Path $Target)) {
                Add-CheckError "$($MarkdownFile.FullName.Substring($RepoRoot.Length + 1)) has missing link $Link"
            }
        }
    }

    foreach ($MarkdownFile in $MarkdownFiles | Where-Object { $_.FullName -match "\\references\\" }) {
        $Lines = Get-Content $MarkdownFile.FullName
        if ($Lines.Count -gt 100 -and -not ($Lines | Where-Object { $_ -eq "## Contents" })) {
            Add-CheckError "$($MarkdownFile.FullName.Substring($RepoRoot.Length + 1)) exceeds 100 lines without a Contents section"
        }
    }

    $PythonScripts = Get-ChildItem $SkillsRoot -Recurse -File -Filter "*.py"
    foreach ($PythonScript in $PythonScripts) {
        & python -c "import ast, pathlib, sys; ast.parse(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))" $PythonScript.FullName
        if ($LASTEXITCODE -ne 0) {
            Add-CheckError "$($PythonScript.FullName.Substring($RepoRoot.Length + 1)) has invalid Python syntax"
        }
    }
    if ($PythonScripts.Count -gt 0) {
        Add-CheckPass "$($PythonScripts.Count) Python scripts parsed successfully"
    }

    if ($CheckInstalled) {
        $InstalledRoot = Join-Path $HOME ".agents\skills"
        foreach ($SkillDir in $SkillDirs) {
            $InstalledSkill = Join-Path $InstalledRoot $SkillDir.Name
            if (-not (Test-Path $InstalledSkill)) {
                Add-CheckWarning "$($SkillDir.Name) is not installed under $InstalledRoot"
                continue
            }

            $WarningCountBefore = $Warnings.Count
            $SourceFiles = @(Get-ChildItem $SkillDir.FullName -Recurse -File | Where-Object {
                $_.FullName -notmatch "__pycache__"
            })
            $InstalledFiles = @(Get-ChildItem $InstalledSkill -Recurse -File | Where-Object {
                $_.FullName -notmatch "__pycache__"
            })
            $SourceRelative = @($SourceFiles | ForEach-Object {
                $_.FullName.Substring($SkillDir.FullName.Length + 1)
            })
            $InstalledRelative = @($InstalledFiles | ForEach-Object {
                $_.FullName.Substring($InstalledSkill.Length + 1)
            })

            foreach ($SourceFile in $SourceFiles) {
                $Relative = $SourceFile.FullName.Substring($SkillDir.FullName.Length + 1)
                $InstalledFile = Join-Path $InstalledSkill $Relative
                if (-not (Test-Path $InstalledFile)) {
                    Add-CheckWarning "$($SkillDir.Name) installed copy is missing $Relative"
                    continue
                }
                if ((Get-FileHash $SourceFile.FullName).Hash -ne (Get-FileHash $InstalledFile).Hash) {
                    Add-CheckWarning "$($SkillDir.Name) installed copy differs at $Relative"
                }
            }

            foreach ($Relative in $InstalledRelative) {
                if ($Relative -notin $SourceRelative) {
                    Add-CheckWarning "$($SkillDir.Name) installed copy has stale extra file $Relative"
                }
            }

            if ($Warnings.Count -eq $WarningCountBefore) {
                Add-CheckPass "$($SkillDir.Name) installed copy matches source"
            }
        }
    }
    Write-Host ""
    Write-Host "Validation summary: $($Errors.Count) error(s), $($Warnings.Count) warning(s)."
    if ($Errors.Count -gt 0) {
        exit 1
    }
}
finally {
    Pop-Location
}
