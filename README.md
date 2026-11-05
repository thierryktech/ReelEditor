# ReelEditor — Balena advertisement and Reel skill for Claude

A reusable Claude Code skill for Balena Roastery: brand-consistent 2D anime stories, exact-product ads, Thai Reel planning, Christmas campaigns, video-model prompts, Remotion planning and FFmpeg export validation.

## Install from GitHub
Clone this repository and start Claude Code from its root:

```sh
git clone https://github.com/thierryktech/ReelEditor.git
cd ReelEditor
claude
```

The project skill lives at `.claude/skills/balena-video/SKILL.md`; invoke `/balena-video` or ask for a Balena video. Claude Code discovers project skills from `.claude/skills/`. See the [official documentation](https://code.claude.com/docs/en/skills).

For another existing project, copy the **whole** `balena-video` folder into that project's `.claude/skills/`. For personal installation, copy it to `~/.claude/skills/balena-video/`. Do not copy only SKILL.md: its references and scripts are required. This repository targets Claude Code; GitHub hosting alone does not install it in the Claude website.

## Examples

```text
/balena-video Create a 16-second Christmas Reel in two connected 8-second parts. Use 2D anime Balena, my original Blue Magic and Original Cold Brew assets, no added text, fully silent. First deliver the shot list and image-to-video prompts. Do not generate paid clips yet.
```

```text
/balena-video Build a product ad from my original packaging PNGs. Use exact labels, bright ivory Christmas scenery, subtle product motion, 1080x1920 at 30 fps. Use Remotion if installed; verify a sample render. Deliver an MP4, editable source and QA report. No added text or audio.
```

```text
/balena-video Edit my cafe footage into a 15-second Thai Reel. Draft a hook and short Thai captions, no voiceover. Ask me to select licensed music before using audio. Preserve product labels. The offer is not confirmed, so do not add a discount.
```

## What is included
- Core workflow and locked character identity.
- Eight-SKU reference mapping and original-artwork compositing rules.
- Two connected Christmas shot recipes plus single-shot retry discipline.
- Remotion/FFmpeg routing, export expectations and honest fallback behavior.
- Editable brief JSON and source-asset fingerprint inventory.
- Standard-library asset inventory and ffprobe-based video checks.
- Technical tests, behavioral evaluation cases and GitHub Actions validation.

## Assets and dependencies
Original images are not embedded in this repository. Use your supplied originals, place copies in ignored `private-assets/`, visually verify each SKU and point the brief to those files. `assets/source-assets.json` records supplied filenames/hashes when available; hashes do not prove label or character accuracy. Avoid publishing source assets in a public repository.

Python 3.10+ runs the helpers and tests. `check_video.py` needs ffprobe from FFmpeg. Remotion needs a separate working Node/React project, browser dependencies and an appropriate license. A video generator needs its own account/API access and credits. The skill does not include a turnkey renderer, a character rig, model credentials or an API subscription.

```sh
python -m unittest discover -s tests -v
python .claude/skills/balena-video/scripts/inventory_assets.py private-assets --output assets-local.json
python .claude/skills/balena-video/scripts/check_video.py final.mp4 --seconds 16 --silent
```

Inventory generation does not edit images. Export validation does not replace visual review.

## Repository and original assets

This skill is maintained at [thierryktech/ReelEditor](https://github.com/thierryktech/ReelEditor). The repository is public. Original artwork, footage, music, credentials and generated campaign renders belong in ignored local folders or an explicitly approved asset store. No brand images are embedded here. The README describes a Claude skill package, not a finished Reel editing application.

## Maintaining the skill
Change identity rules only when the brand reference changes. Update product mappings from verified artwork, not inferred filenames. Add a behavioral regression case whenever a prompt yields a recurring mistake. Keep commercial terms campaign-specific. Never hard-code model prices or historical discounts. The brand artwork remains the owner's property; no redistribution license is granted by this repository.

Documentation checked: 2026-11-05. Official references are linked in the skill's production guide; verify current APIs, plan entitlements and licensing when needed.
