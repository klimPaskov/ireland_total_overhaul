# Ireland optional audio research

Feature slug: `ireland_focus_tree`

Research date: 2026-07-18

This note contains exactly three optional concepts, matching the canonical prompt: coastwatch/Atlantic ambience, a constitutional or sacral High Kingship ceremony cue, and a verified Otherworld entry cue. Audio is never a mechanical prerequisite. No sound definition, gameplay, localisation, or asset file is changed here.

## Clearance vocabulary

These are research statuses, not legal opinions:

- **A1 — documented source candidate:** the source page states a public-domain or CC0 grant. Preserve the page URL, creator name, and downloaded original before shipping; inspect the recording for incidental third-party material.
- **C1 — commissioning-safe brief, not cleared:** the brief is safe to send to a composer/performer, but no rights exist until the commission is accepted, the work is delivered, and the contract covers both the composition and the recording/master.

## Summary

| Concept | Provenance | Composition rights | Recording rights | Clearance state/tier | Suggested final OGG |
| --- | --- | --- | --- | --- | --- |
| `coastwatch_atlantic_ambience` | Dún Laoghaire, County Dublin field recording by danlj | No composed music; screen any incidental audible material | CC0 1.0 as stated on the source page | Documented candidate, A1; not downloaded or locally verified | `sound/ireland/ireland_coastwatch_atlantic_ambience.ogg` |
| `high_kingship_ceremony` | Original commission brief for a constitutional/sacral ceremony | New composition; contract required | New performance/master; contract required | Commissioning-safe brief, C1; not cleared and no audio exists | `sound/ireland/ireland_high_kingship_ceremony.ogg` |
| `otherworld_entry` | Original commission brief for a verified, evidence-led passage | New composition; contract required | New performance/master; contract required | Commissioning-safe brief, C1; not cleared and no audio exists | `sound/ireland/ireland_otherworld_entry.ogg` |

## 1. Coastwatch and Atlantic ambience

### Candidate

- **Title:** `Dun Laoghaire Harbour on a windy day`
- **Creator / recording source:** danlj; field recording made at Dún Laoghaire Harbour, County Dublin, Ireland, on 19 March 2022. There is no performer or separate musical composition.
- **Source:** [Freesound source page](https://freesound.org/people/danlj/sounds/624753/)
- **Source description:** waves breaking against the shore with moderate-to-strong wind; the creator identifies the location and recording equipment on the source page.
- **Source duration and format:** 20:00.000, WAV, 96 kHz, 24-bit, stereo, approximately 660 MB.
- **Licence:** [Creative Commons CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), as displayed on the source page. The page permits copying, modification, distribution, and performance, including commercial use, without requesting permission.
- **Licence confidence:** high for the displayed recording licence; still conditional on preserving the source-page record and screening the downloaded waveform for incidental third-party material.
- **Attribution:** not required by CC0; retain `danlj — Dun Laoghaire Harbour on a windy day` and the source URL in the project manifest as provenance.
- **Composition versus recording:** this is a field recording rather than a musical composition, so the relevant rights layer is the recording. Before release, listen through the selected segment and reject or trim it if voices, identifiable broadcasts, or other third-party material are audible.
- **Clearance state/tier:** documented source candidate, **A1**. It is not locally cleared yet because this research pass did not download, hash, or inspect the file.
- **Original source path:** not downloaded. If approved, preserve the unmodified download at `docs/plans/ireland_focus_tree/audio_research/source/danlj_624753_dun_laoghaire_harbour.wav`.
- **Suggested final OGG path:** `sound/ireland/ireland_coastwatch_atlantic_ambience.ogg`.
- **Suggested id:** `ireland_coastwatch_atlantic_ambience`.
- **Intended use:** low-volume ambience for a dedicated maritime or National Conditions surface showing coastwatch, shipping, weather, or rescue information. It should reinforce Ireland's exposed coastline without becoming a route anthem.
- **Edit and conversion plan:** retain the original WAV; choose a clean 60-second passage with a stable wave bed, trim only at matching wave cycles, and use a short equal-power crossfade at the loop seam. Convert the approved segment to the repository's OGG Vorbis convention, targeting 44.1 kHz stereo. Do not loop the full twenty-minute source in the UI.
- **Loop needs:** seamless loop, approximately 60 seconds; no musical intro or outro. Stop playback when the maritime surface closes.
- **Static/no-audio behavior:** the surface remains fully usable with its static map/art, text, and values when this optional sound is absent. Do not substitute a default or placeholder sound, and do not let a missing audio file block coastwatch decisions, missions, or conclusions.
- **Fit note:** this is unusually strong provenance for an Ireland feature because the recording itself is from County Dublin, while the long, high-resolution source gives the implementation owner room to choose a non-repetitive loop.

## 2. Constitutional or sacral High Kingship ceremony cue

### Commissioning-safe concept: `The Crown at Tara` (working title)

- **Creator / composer:** to be commissioned; no composer is implied by this working title.
- **Performer / recording source:** a commissioned harp-led ensemble or soloist, with any additional performers named in the contract. No pre-existing recording, sample pack, anthem, or film/game score should be used.
- **Source / brief path:** this section of `docs/plans/ireland_focus_tree/audio_research/ireland_optional_audio_research.md`; there is no external source recording.
- **Provenance:** original work commissioned specifically for the Ireland High Kingship conclusion or a constitutional/sacral ceremony presentation. The brief is a source document, not a claim that a finished recording exists.
- **Composition rights:** require a worldwide, perpetual, royalty-free licence or assignment covering the composition, arrangement, edits, synchronisation with the mod, distribution with the mod, and promotional previews. The composer must warrant that the melody, arrangement, and any text are original or separately cleared.
- **Recording/master rights:** obtain the same scope from every performer and session contributor, including permission to edit, fade, encode, loop if needed, and distribute the master. Prohibit uncleared samples, stock loops, generative imitation of a named performer, and unlisted collecting-society restrictions.
- **Licence confidence:** none for a final asset until the commission contract is signed and the delivered composition, performers, stems, and master are checked against it.
- **Clearance state/tier:** commissioning-safe brief, **C1**. It is not cleared; no audio may ship until the written rights grant and final source/master files are in hand.
- **Original source path:** no source recording exists. Store the signed brief, contract, stems, and delivered master under `docs/plans/ireland_focus_tree/audio_research/source/high_kingship_commission/` if a commission is approved.
- **Suggested final OGG path:** `sound/ireland/ireland_high_kingship_ceremony.ogg`.
- **Suggested id:** `ireland_high_kingship_ceremony`.
- **Intended use:** a one-shot presentation cue for the constitutional or sacral High Kingship ceremony/conclusion, not a normal country music track and not a recurring GUI ambience.
- **Musical brief:** 60–75 seconds; solemn, deliberate, and public-facing. Begin with a restrained harp or plucked-string gesture, develop through a measured processional pulse, and resolve with an earned final cadence. Keep the sound civic and ceremonial rather than militaristic; avoid quoting or closely imitating a national anthem, a recognisable traditional tune, or a commercial fantasy score. Instrumental or non-lexical voice is preferred so no lyric/text-rights layer is introduced.
- **Format and edit needs:** request full-mix and dry stems as 48 kHz, 24-bit WAV; deliver the final as repository-approved 44.1 kHz stereo OGG Vorbis. Apply a short fade-in and 2–3 second tail fade; no loop is needed.
- **Static/no-audio behavior:** the conclusion still presents its static proclamation art, text, and route result without sound. No route, achievement, or country-state change may wait for the cue or fail when the optional audio package is omitted.
- **Fit note:** commissioning avoids assigning a modern recording to a fictional monarchy and keeps the cue distinct from republican, military, or church source music while still allowing a grounded Irish harp-led identity.

## 3. Verified Otherworld entry cue

### Commissioning-safe concept: `The Road That Has No Map` (working title)

- **Creator / composer:** to be commissioned from a composer/sound artist with the brief below; no existing artist is implied.
- **Performer / recording source:** commissioned performers and/or the composer using newly recorded acoustic material. Do not sample a film, game, commercial library, or an unverified traditional recording.
- **Source / brief path:** this section of `docs/plans/ireland_focus_tree/audio_research/ireland_optional_audio_research.md`; there is no external source recording.
- **Provenance:** original work for the verified Otherworld entry presentation after the evidence, witness, site, and consequence requirements have been met. The cue must not be used to prove the route or announce an unverified clue.
- **Composition rights:** contract must cover the original composition, arrangement, edits, stems, synchronisation, mod distribution, trailers/previews, and future re-encoding. The composer must warrant no unlicensed quotations, samples, or close imitation of an identifiable copyrighted soundtrack.
- **Recording/master rights:** every performer and contributor must grant the same distribution and editing permissions for the master and stems; the contract must permit a quiet mix and a short tail edit.
- **Licence confidence:** none for a final asset until the commission contract is signed and the delivered composition, performers, stems, and master are checked against it.
- **Clearance state/tier:** commissioning-safe brief, **C1**. It is not cleared; no audio exists until the commission and rights paperwork are complete.
- **Original source path:** no source recording exists. Store the signed brief, contract, stems, and delivered master under `docs/plans/ireland_focus_tree/audio_research/source/otherworld_commission/` if a commission is approved.
- **Suggested final OGG path:** `sound/ireland/ireland_otherworld_entry.ogg`.
- **Suggested id:** `ireland_otherworld_entry`.
- **Intended use:** a one-shot reveal cue for a verified Otherworld entry, passage, or return presentation. It should never play for ordinary folklore research, a false lead, or a merely speculative event.
- **Musical brief:** 45–60 seconds; evidence-led rather than spectacle-led. Use a clear human performance or newly captured acoustic source, with sparse harp/string resonance, restrained frame-drum or wood/percussion punctuation, and an unsettling but coherent harmonic turn. Avoid generic fairy sparkle, horror stingers, spoken lore quotations, and a continuous noise bed. The emotional arc should be recognition, obligation, and consequence—not a free reward.
- **Format and edit needs:** request full-mix and dry stems as 48 kHz, 24-bit WAV; deliver the final as repository-approved 44.1 kHz stereo OGG Vorbis. Use a short fade-in only if the presentation needs it and leave a 1–2 second tail; no loop is needed.
- **Static/no-audio behavior:** the verified reveal remains readable and playable through static art, evidence text, and the normal conclusion/result presentation without sound. Audio absence must not weaken verification, grant a route benefit, alter obligations, or suppress the event.
- **Fit note:** a bespoke, non-imitative recording respects the specification's requirement that the impossible route be grounded in evidence and consequences rather than borrowing a familiar fantasy soundtrack or presenting folklore as automatic truth.

## Exact wiring handoff

The main implementation agent owns sound definitions and trigger wiring. The following ids and paths are recommendations only; no definition has been added here.

| Suggested id | Proposed file | Surface and trigger | Playback | No-audio rule |
| --- | --- | --- | --- | --- |
| `ireland_coastwatch_atlantic_ambience` | `sound/ireland/ireland_coastwatch_atlantic_ambience.ogg` | Start when the dedicated maritime/National Conditions surface opens; stop when it closes | Low-volume loop, target 60 seconds | Skip the sound call entirely if the optional file is absent; keep the surface and all maritime mechanics active |
| `ireland_high_kingship_ceremony` | `sound/ireland/ireland_high_kingship_ceremony.ogg` | Fire once from the High Kingship constitutional/sacral ceremony or conclusion presentation after its normal route result is determined | One-shot, 60–75 seconds, no loop | Present the static ceremony/conclusion normally and do not substitute an anthem or placeholder |
| `ireland_otherworld_entry` | `sound/ireland/ireland_otherworld_entry.ogg` | Fire once only from the verified Otherworld entry/reveal presentation after verification succeeds | One-shot, 45–60 seconds, no loop | Present the static reveal/evidence/consequence result normally; never make audio part of verification or reward logic |

## Blockers and uncertainty

- The Dún Laoghaire recording is a strong, rights-documented candidate, but it was not downloaded or waveform-screened in this research-only pass. Preserve the source page and inspect the chosen segment before release.
- The High Kingship and Otherworld entries are safe commissioning briefs, not cleared audio. They require written composition and recording/master rights before implementation can ship them.
- No `.ogg` was created, and no source file was placed in this folder. The proposed source and final paths above are handoff paths only.
- All three concepts are optional. No route, achievement, conclusion, decision, mission, or GUI surface should depend on the presence of an audio file.
