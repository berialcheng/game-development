# Steam Sources

Use this reference when researching a game from Steam.

## Primary Inputs

Store page:

```text
https://store.steampowered.com/app/<APPID>/<slug>/
```

Appdetails API:

```text
https://store.steampowered.com/api/appdetails?appids=<APPID>&l=english
```

Useful fields commonly returned by `appdetails`:

- `success`
- `data.name`
- `data.type`
- `data.short_description`
- `data.about_the_game`
- `data.detailed_description`
- `data.header_image`
- `data.capsule_image`
- `data.screenshots[].path_full`
- `data.screenshots[].path_thumbnail`
- `data.movies[]`
- `data.genres[]`
- `data.categories[]`
- `data.developers[]`
- `data.publishers[]`
- `data.release_date`
- `data.price_overview`

## Extraction Procedure

1. Confirm the app id and title.
2. Fetch `appdetails` and require `success=true`.
3. Extract official text: short description, about text, feature bullets, genres, categories.
4. Extract official media: header, capsule, screenshots, movie thumbnails/videos.
5. Open the rendered store page when the API omits page text, tags, reviews, community links, or DLC/bundle context.
6. Use HEAD or a small request to verify image URLs return status 200 and an image content type when collecting links.

## Design Signals

Steam text:

- One-line positioning and genre promise.
- Explicit verbs such as drag, build, fight, sell, craft, explore, survive.
- Progression counts such as cards, quests, bosses, biomes, unlocks.
- Failure pressure such as hunger, timer, waves, permadeath, enemies.
- Session duration or content scale if stated.

Steam tags:

- Market positioning and player expectation.
- Adjacent genre references for competitor selection.
- Do not treat tags as exact mechanics; validate with text/media.

Steam categories:

- Platform and feature support such as single-player, co-op, achievements, workshop, controller, cloud.
- Useful for product scope, not gameplay detail.

## Reliability

- Official store text: high confidence for intended features.
- `appdetails`: high utility, medium stability; it is practical but not a formal design contract.
- CDN screenshots: high confidence as official marketing media when linked from store/API.
- Review counts and prices are time-sensitive; re-fetch when reporting them.
