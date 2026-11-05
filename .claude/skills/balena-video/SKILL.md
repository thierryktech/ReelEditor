---
name: balena-video
description: Create Balena Roastery product advertisements, Instagram Reels, anime mascot stories, storyboards, video-generation prompts, and rendered video edits. Use for Balena video campaigns requiring accurate whale proportions, original product labels, Thai copy, Christmas styling, or Remotion and FFmpeg production.
---

# Balena video production

Turn the user's brief into an executable production package or a verified rendered video. A skill supplies instructions and scripts; it does not itself supply video-model access, API credits, or a rendering service. Never claim a video exists when only its prompt or storyboard exists.

## 1. Resolve the brief

Read [brand identity](references/brand-identity.md) and [product integrity](references/product-integrity.md) for every campaign. Read [production](references/production.md) for rendering and [prompt recipes](references/prompt-recipes.md) for generated clips. Consult [quality gates](references/quality-gates.md) before delivery.

Use explicit current instructions over defaults. Reuse visible project facts; ask only for unresolved information that blocks accurate work. Continue story development while waiting for missing assets or commercial terms.

Classify the requested deliverable: concept, storyboard, generation prompt, edit existing footage, render an ad, or reusable campaign template. Do not generate or purchase media merely because the user requested a prompt.

Create `brief.json` from `assets/brief.example.json`, replacing example selections with real selected assets. Record objective, audience, placement, style, duration, products, assets, text policy, audio policy, offer, CTA, deliverables, and renderer. Mark unknown facts as unknown. Historical offers are not current authorization.

Defaults when unspecified:
- Instagram Reel: 1080 x 1920, 9:16, 30 fps.
- Mascot story: 16 seconds in two connected 8-second parts; use 8 seconds if requested.
- Visual style: hand-drawn 2D anime, clean linework, cel shading, soft painted scenery. No 3D default.
- Mascot campaign: no added text, no music, no speech, no sound effects; fully silent.
- For footage Reels, confirm whether Thai captions and music are wanted; do not assume the mascot silence policy is a universal brand rule.
- Render draft only. Publishing, scheduling, spending credits and uploading externally require the user's task authorization.

## 2. Verify assets before planning motion

Identify the canonical character reference and each exact product. Inspect images rather than relying on filenames. Use the asset manifest and SHA-256 fingerprints to track originals. A fingerprint proves file identity, not visual correctness. If the canonical mascot reference is unavailable, continue storyboarding and product composition, but obtain it before claiming exact Balena character fidelity. Do not automatically substitute a tiny mascot printed on a product label for the canonical sheet.

Do not substitute a different SKU, redesign a label, mirror the spout, or invent unreadable label text. Missing original assets block an exact-product render, but not a clearly labeled concept.

Keep original product images as separate layers. Animate their position, scale, or subtle rotation without generative repainting. A requested 2D world may contain original photographic product cutouts: label accuracy takes priority over redrawing the package. If the user requires fully illustrated packaging, explain the accuracy tradeoff and retain the original label artwork as an overlay.

The included `assets/source-assets.json` records provided references. Source artwork is intentionally not embedded in this code repository. Ask for access to the named originals when unavailable. Use `scripts/inventory_assets.py` to create a new inventory for a chosen directory.

## 3. Build a story with a sales purpose

Write a one-sentence idea, then a timed shot table: start/end, customer-facing beat, composition, Balena action, selected products, camera, transition, audio. Use one clear action per generated shot. Establish the product or emotional hook in the first 2–3 seconds. End with a clean product hero hold and a permitted CTA, or a visual invitation when text is prohibited.

For 16 seconds, use two 8-second parts with matching last/first frame: same scene, palette, product arrangement, character size and camera direction. Keep total frames exact (480 at 30 fps). A simple plan is 0–2 hook, 2–6 discovery, 6–8 handoff; 8–12 reveal, 12–14 interaction, 14–16 hero hold. Adjust to the brief.

Do not crowd eight products into a tiny shot and claim label legibility. Use selected hero products, multiple shots, or a product carousel if all SKUs must appear. Preserve the distinction between a Christmas concept box and a real gift-set offer.

## 4. Choose the production route

| Need | Route |
| --- | --- |
| Exact labels, layouts, timing, repeatable campaign variants | Remotion composition using original asset layers |
| Trim, concatenate, encode, resize, audio operations | FFmpeg |
| Expressive anime whale action or changing scenery | Available image-to-video model, then composite exact products |
| Prompt only | Deliver shot prompts, reference assignments and rejection criteria |
| No renderer/model available | Deliver source and instructions; state rendering is pending |

Preflight installed tools and permissions. Do a short sample render before a full export. Use an existing repository's dependency versions and lockfile. Never report Remotion usage if the actual render used another pipeline. Do not repeatedly retry a blocked install without new evidence.

Remotion/FFmpeg do not generate new character poses from a still image. A whole-image pan or wiggle is a motion graphic, not articulated animation. For expressive motion obtain an approved pose sequence, layered rig, or generated clip. Keep fins small and move props closer rather than stretching anatomy.

## 5. Execute, inspect and deliver

Read the route-specific references. Save editable source, original-asset manifest, brief, shot list, prompts when applicable, MP4, cover, and QA report as requested. Do not overwrite unrelated user work.

Run `scripts/check_video.py OUTPUT --seconds <brief-duration> --width <brief-width> --height <brief-height> --fps <brief-fps> --silent` for a silent brief; omit `--silent` when audio is permitted. Substitute actual numeric values from the brief. It checks measurable export properties only. Also inspect start, each shot midpoint, cuts, and last frame; watch the full clip for temporal defects. Compare product labels against the source at useful viewing scale. Use the report format in the quality reference. Mark visual checks NOT RUN when not performed.

For Thai text, use an approved Thai-capable font and inspect shaping, line breaks and mobile readability. No added captions means no captions in any language; original package printing remains intact.

Return the actual deliverable, a concise account of what changed, validation performed, and any remaining limitation. Never claim guaranteed model fidelity or claim a publish/upload succeeded without observing it.
