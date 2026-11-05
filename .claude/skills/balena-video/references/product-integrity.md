# Original-product integrity

## Identify the selected SKU
| Product | Reference appearance | Critical distinction |
| --- | --- | --- |
| Ethiopia Gediyo | Red bag, berry label | Preserve supplied spelling Gediyo |
| Blue Magic | Turquoise bag, blueberry artwork | Not 52 Hz |
| Vino Rosso | Red bag, wine-themed label | Not Ethiopia |
| Whiskey | Gold bag, whiskey-themed label | Not Brazil Cerrado |
| Brazil Cerrado | Gold bag, chocolate/hazelnut imagery | Not Brazil Santos; filenames may say Brasil |
| House Blends | Black bag, beans/chocolate imagery | Preserve plural Blends |
| Cold Brew Original | White spout pouch, cream/blue whale label, 500 mL | Not Smooth Black |
| Cold Brew Smooth Black | White spout pouch, navy night label, 500 mL | Not Original |

This is a reference mapping, not an inventory or guarantee of current availability. Other uploaded products require independent verification. Copy weights, roast level, process, origin and tasting notes from the exact chosen reference, never another SKU. A name alone is not sufficient to distinguish versions.

## Composite rules
Keep the source artwork byte-for-byte in the asset folder. Use its alpha channel or a non-destructive mask for the surrounding background. Never remove a background by keying all white pixels: that destroys white labels and pouches. If a source lacks transparency, create and inspect a mask while retaining the unmodified original. Do not mistake black transparency preview for a real black background.

Preserve packaging proportions, seal ridges, gussets, pouch contours, material and artwork placement. Front-view cold-brew pouches have spout upper left and handle upper right. Do not mirror. Keep labels front-facing enough to read. No invented QR patterns or social icons; source QR remains artwork and is not guaranteed scannable after video downscaling.

Position original images above generated scenery. Avoid asking a video model to animate a finished composition that already includes tiny label text. If a generated scene contains package placeholders, replace and occlude them cleanly in the edit. Keep shadows and lighting on separate layers where possible.

Exact artwork preservation does not imply every tiny line is readable on a phone. Report whether each hero product is legible and how long it remains on screen. Do not assert pixel equality after scaling, compression or perspective; preserve the source and document transformations instead.
