# Validation record

Checked on 2026-11-05.

- Skill frontmatter validator: passed.
- Nine Python tests: passed (asset hashing, missing inputs, expected export, unwanted audio, wrong dimensions/duration, invalid probe values, missing streams, references and JSON templates).
- Actual FFmpeg/ffprobe smoke test: passed for a temporary 0.2-second 1080x1920, 30fps, H.264/yuv420p, silent MP4. This was a synthetic color test, not a Balena advertisement.
- Independent instruction walkthrough: reviewed an 8-second/eight-product/no-mascot-reference case. Fixed the duration example and clarified missing-reference behavior. This was an instruction review, not execution inside Claude.
- Full Claude runtime installation, paid model generation, Remotion rendering, GitHub Actions and production creative visual QA: not run.
- GitHub target: thierryktech/ReelEditor. Publication and CI execution must be verified against the actual remote result.
