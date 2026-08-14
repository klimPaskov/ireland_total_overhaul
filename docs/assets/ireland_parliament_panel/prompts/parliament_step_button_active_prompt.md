# Ireland Parliament active button prompt

Use case: precise-object-edit

Asset type: Hearts of Iron IV scripted-GUI button texture

Input image: the existing Ireland Parliament active-state step button.

Edit the existing asset while preserving its long rounded 204x32 silhouette,
border placement, transparent outside corners, bevels, and empty text-safe
centre. Make only the active face visibly brighter and more saturated: rich
Irish emerald and bottle-green enamel with a subtle centre highlight. Strengthen
the warm antique-brass inner and outer rim so it remains legible at final size.
Retain the restrained 1930s government-dossier style. It must read as green,
active, and clickable without becoming neon. Include no text, icon, symbol,
watermark, protrusion, or additional object.

The built-in image-generation edit produced the RGB source at 1983x793. Its
button field is cropped, alpha-cleaned against the black exterior, and resized
with Lanczos resampling to the exact 204x32 runtime dimensions before DDS
conversion. Engine `buttonstate.lua` remains responsible for hover, pressed,
and disabled variants.
