# Delivery quality gates

## Machine checks
Validate brief JSON and actual asset paths. Check duration within one frame, expected resolution/fps, H.264 MP4, yuv420p, and silent/no-audio policy. `scripts/check_video.py` covers those properties; a passing result is not a visual review. Check faststart/export flags from the actual render command if required; the script does not inspect MP4 atom order.

## Visual and temporal checks
Watch the full clip, inspect first/last frames, shot midpoints, every cut and the 8-second join. Use frame stepping for flicker, clipping, occlusion and sudden scale changes. Compare the whale to the canonical reference: squat wide form, no feet/neck, correct cup, splash, cheeks and belly. Check every displayed SKU against the source: name, label artwork, weight where visible, pouch shape and spout orientation. Ensure ribbons and hands/fins never cover key information. Inspect white balance and preserved white-pouch detail. Confirm the story has a hook, clear reveal and final hold.

For Thai text inspect actual rendered shaping, not only the source string. For no-text work confirm absence of overlays, including accidental question marks, captions and watermarks. Original printing is allowed unless the user explicitly requests blank labels, which conflicts with exact original packaging and must be resolved.

## Report template
- Deliverable and actual renderer/model:
- Brief deviations and why:
- Technical checks: PASS / FAIL with measured values:
- Original references and selected SKUs:
- Character review: PASS / FAIL / NOT RUN:
- Product-label review: PASS / FAIL / NOT RUN:
- Full playback and transitions: PASS / FAIL / NOT RUN:
- Text/audio policy: PASS / FAIL / NOT RUN:
- Remaining limitations:
- Files delivered and pending work:

Failing critical anatomy, wrong SKU, rewritten artwork, unauthorized offer or unintended audio blocks final approval. Fix before delivering as final, or clearly identify a draft. Do not hide NOT RUN checks behind “QA passed.”
