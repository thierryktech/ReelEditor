# Production routes

## Preflight
Check `node --version`, package manager, local package.json/lockfile, Remotion installation, browser dependencies, `ffmpeg -version` and `ffprobe -version` as relevant. Network access and a Claude subscription do not imply access to a video model or a free Remotion commercial license. Check current official license terms for the user's use case before advising deployment; do not hard-code prices.

## Remotion
Use React/TypeScript with a fixed composition fps, width, height and durationInFrames. Prefer frame-driven transforms via `useCurrentFrame`, `interpolate`, `spring`, `Sequence`, `Img` and `staticFile`; check current API docs before introducing unfamiliar calls. Keep input props separate from animation code: selected product assets, colors, timed shots, permitted captions and audio. Use original assets in `public/` or resolved permitted URLs. Use `objectFit: contain`; avoid cropping labels. Bound spring/transform motion and keep package scale stable during hero holds.

Pin actual dependencies with a lockfile; do not invent a known-working version. A typical existing project uses `npx remotion compositions` to inspect IDs and `npx remotion render <entry> <composition-id> <output.mp4>` to render; derive actual arguments from that project's scripts/current CLI. Render a short preview before full length. Do not describe an unexecuted template as tested. No mandatory npm install or public cloud render.

## FFmpeg
Use argument arrays in scripts rather than shell-string interpolation. Inspect inputs with ffprobe. For an existing SDR edit, an example final export is:

```sh
ffmpeg -i edit.mp4 -an -c:v libx264 -pix_fmt yuv420p -movflags +faststart final-silent.mp4
```

This encodes a silent MP4; it does not create missing scenes, alter duration, or guarantee 1080x1920. Set dimensions/fps/duration intentionally in the composition/edit. Do not stretch a horizontal source to vertical; crop with subject-aware framing or pad. Check whether cropping removes products. Retain the original.

HDR footage needs an intentional HDR-to-SDR color transform and metadata handling, not just an SDR tag. Inspect color transfer/primaries and available tone-map filters; test the conversion visually. Do not apply one blind filter to all footage. For audio-enabled work use approved/licensed assets, trim/fade appropriately, prevent clipping and export compatible AAC. Silent work should have no audio stream.

## Output structure
`campaigns/<campaign-id>/brief.json`, `storyboard.md`, `prompts.md` when relevant, `assets-manifest.json`, editable source, `renders/preview.mp4`, `renders/final.mp4`, `renders/cover.png`, `qa.md`. Use source control for source/config; keep originals and renders out of public git unless explicitly authorized. Do not commit tokens, signed URLs, personal data or licensed music.

## Layout
Use 1080x1920 unless requested otherwise. As a conservative design assumption, start with 90 px side padding, 220 px top clearance and 360 px bottom clearance for critical overlays, then preview in the intended placement. These are adjustable design margins, not official universal Instagram safe zones. Do not shrink products into illegibility to satisfy arbitrary margins.

## Current official references
- https://www.remotion.dev/docs/ — React rendering and export APIs
- https://www.remotion.dev/license — commercial licensing
- https://ffmpeg.org/ffmpeg.html — CLI
- https://ffmpeg.org/ffprobe.html — inspection
- https://ffmpeg.org/ffmpeg-filters.html — filters/color handling
