# Ireland focus tree text research handoff

Feature slug: `ireland_focus_tree`  
Research role: bounded quote, remark, slogan, title-reference, and provenance research  
Date: 2026-07-18  
Scope: text research only. No localisation, gameplay, GUI, GFX, sound definition, or implementation files were edited.

This note follows the canonical [Ireland text and audio research prompt](../../../specs/ireland_focus_tree/prompts/ireland_focus_tree_text_audio_research_prompt.md). It is a source and clearance handoff, not final event prose. The twelve package labels below are the working labels in that prompt; they are not implementation identifiers.

## Source and clearance key

| Mark | Meaning |
| --- | --- |
| `A1` | Primary official text: statute, Constitution, Dáil record, diplomatic document, or official ecclesiastical text. |
| `A2` | Primary archival item, archival catalogue, scan, or institutional collection record. Wording may still require permission to reproduce. |
| `B` | Reputable academic, archival, or historical publication reproducing or describing a primary source. Exact wording is mediated unless the primary item is linked. |
| `C` | Search lead, popular retelling, quotation site, or attribution not independently verified. Do not ship as a direct quotation. |
| `low` | Short title or short historical/legal fragment; ordinary source credit is sufficient in the research record, subject to territorial/editorial review. |
| `check` | Short use is plausible, but the host archive, edition, scan, or translation has reproduction terms that should be checked before display. |
| `restricted` | Do not reproduce without permission; use only a title, paraphrase, or a separately cleared short fragment. |
| `reject` | Do not use as a quotation. Attribution, wording, or feature fit is not secure. |

“Public domain” below means the underlying historical text or title is old enough to be a strong low-risk candidate; it does not waive the rights of a modern scan, scholarly translation, archive transcription, or website. Modern copyrighted audio and broadcast material is not needed for this text-only handoff.

## Executive recommendation

### Selected main quote

> “to develop its life, political, economic and cultural, in accordance with its own genius and traditions.”

Speaker/author: the phrase is Article 1 constitutional language in the de Valera-led draft Constitution; it is attested in Éamon de Valera’s Dáil presentation of the draft on 11 May 1937.  
Work/source: [Bunreacht na hÉireann, Dáil debate, 11 May 1937](https://www.oireachtas.ie/en/debates/debate/dail/1937-05-11/29/) and the [Irish Statute Book Constitution text](https://www.irishstatutebook.ie/eli/cons/en/html).  
Date: 1937; the Constitution was approved by referendum on 1 July and came into operation on 29 December 1937.  
Source tier: `A1`. Attribution confidence: wording `high`; personal authorship by de Valera `medium`, because this is enacted constitutional language rather than a free-standing personal aphorism. Clearance: `low` for this short legal fragment, with source credit retained.

Fit: this is the strongest single feature-wide text because it can sit above constitutional, economic, cultural, language, neutrality, and regional material without announcing a route. It sounds like sovereignty and obligation rather than generic nationalism. Keep the fragment attached to Constitution, Dáil, or civic-development surfaces; do not label it as a verbatim private speech by de Valera.

### Selected cultural remark/allusion

> *The Celtic Twilight*

Speaker/author: W. B. Yeats.  
Work/date: *The Celtic Twilight*, 1893.  
Source: [Project Gutenberg edition and metadata](https://www.gutenberg.org/ebooks/10459); the National Library of Ireland also documents Yeats’s folklore work and the Irish Literary Revival in its [1916 exhibition](https://www.nli.ie/1916/exhibition/en/content/stagesetters/culture/).  
Source tier: `A2/B` for the title and cultural context. Attribution confidence: `high`. Clearance: `low` for title-only use; the Project Gutenberg page says its edition is public domain in the United States, so the main agent should still clear any longer excerpt by territory and edition.

Fit: use as a title-like cultural reference for the serious folklore, memory, and Otherworld evidence lane. It is preferable to an invented “Celtic” slogan because it is an attested work title and can carry both admiration and skepticism. It should not imply that Yeats’s occult or folkloric framing was a state policy, or that supernatural claims are established facts.

### Recommended short Otherworld evidence remark

> “There is a fort at the back of our garden in Fairymount.”

Source: a [Dúchas Schools’ Collection entry from Fairymount, County Roscommon](https://www.duchas.ie/en/cbes/4798671/4789009/4862310), collected in the 1937–39 Schools’ Collection. The page identifies the National Folklore Collection, collector Máire Ní Ríagáin, and local material; the precise speaker/entry attribution is not clear enough to name a speaker in a UI string.  
Source tier: `A2`; wording confidence `high`; speaker confidence `medium`; clearance: `low/check` because the page marks the open-data material CC BY 4.0, but the attribution and exact transcription should remain with the archive record.

Fit: this is a testimony/evidence line, not a supernatural assertion. It is suitable for a hidden investigation, local witness report, folklore collection, or regional event. The feature prompt’s “evidence first” rule should be followed: show a place, testimony, damaged site, or consequence before introducing an impossible interpretation.

## Main-quote comparison

Several candidates were compared before selecting the constitutional fragment.

| Candidate | Provenance and fit | Decision |
| --- | --- | --- |
| Article 1 fragment, “to develop its life ... in accordance with its own genius and traditions” | De Valera-led 1937 constitutional text; supports constitutional, cultural, economic, and sovereignty surfaces. `A1`, high wording confidence, `low` clearance for a short legal fragment. | **Selected.** Broadest fit and safest attribution when labelled constitutional language. |
| “Éire is determined to preserve her neutrality and stay out of the war if humanly possible.” | De Valera position recorded in a 1940 diplomatic document quoting a contemporary interview. [DIFP, 5 July 1940](https://www.difp.ie/volume-6/1940/emphasise-irish-determination-to-remain-neutral/3235/). `A1`, high, `low/check`. | Best wartime backup; narrower than the selected quote. |
| “Of our own free decision and in our own interests, we have come here to gain greater strength and wider opportunity” | Seán Lemass, opening of the European Economic Cooperation conference, 14 July 1947. [DIFP vol. 8](https://www.difp.ie/volume-8/1947/speech-by-sean-lemass-to-the-opening-session-of-the-conference-on-european-economic-co-operation/4466/). `A1`, high, `low/check`. | Best development/economic backup; post-start-date and less useful for folklore or constitutional identity. |
| “the fruit of the steady, persistent attack against the State and its fundamental institutions” | W. T. Cosgrave after Kevin O’Higgins’s assassination, 1927; confirmed by the [Oireachtas notable-debates record](https://www.oireachtas.ie/en/debates/notable-debates/) and contemporary press reproduction. `A1/B`, high, `low/check`. | Strong security/civil-war-memory text; too confrontational for a feature-wide main quote. |
| “This Bill burns no bridges leading either to national unity or to closer friendship with the people of our neighbouring country” | John A. Costello, Republic of Ireland Bill debate, 24 November 1948. [Dáil record](https://www.oireachtas.ie/en/debates/debate/dail/1948-11-24/51/). `A1`, high, `low/check`. | Strong coalition/republic backup; late-period and tied to one bill. |
| “living our own lives in our own country, and developing our own resources” | Richard Mulcahy, Treaty debate, 22 December 1921. [Dáil record](https://www.oireachtas.ie/en/debates/debate/dail/1921-12-22/2/). `A1`, high, `low/check`. | Strong self-government and defence-capacity fragment; not as encompassing. |

## Leader voice ledger

These are real, separately sourced voices. Do not merge their diction into a generic “Irish statesman” voice.

### Éamon de Valera

1. **Constitutional voice — preferred.** The selected Article 1 fragment above is supported by the [11 May 1937 Dáil debate](https://www.oireachtas.ie/en/debates/debate/dail/1937-05-11/29/). It should be labelled as constitutional language or as de Valera presenting the draft, not as an unqualified personal maxim. Tone: sovereignty, national self-determination, cultural development, and “genius and traditions.”
2. **Neutrality backup.** “Éire is determined to preserve her neutrality and stay out of the war if humanly possible.” Source: [DIFP, de Valera position, 5 July 1940](https://www.difp.ie/volume-6/1940/emphasise-irish-determination-to-remain-neutral/3235/). Tone: determination and freedom of action. `A1`, confidence `high`, clearance `low/check`.
3. **Emergency/treason backup.** De Valera told the Dáil in February 1939 that the Constitution gave treason a new meaning and connected national life with Ireland’s “own genius and traditions.” Source: [Treason Bill debate, 23 February 1939](https://www.oireachtas.ie/en/debates/debate/dail/1939-02-23/9/). Use only a short, verified fragment after checking the speaker heading and exact punctuation.
4. **Do not use as a clean direct quote without rights clearance:** RTÉ’s 1943 “The Ireland That We Dreamed Of” material is a real de Valera broadcast, but the [RTÉ archive page](https://www.rte.ie/archives/exhibitions/eamon-de-valera/719124-address-by-mr-de-valera/) states that reproduction requires licensing. The title is a usable allusion; a displayed excerpt is `restricted` until RTÉ clearance.

### Seán Lemass

Preferred quote: “Of our own free decision and in our own interests, we have come here to gain greater strength and wider opportunity.” This is a short fragment from Lemass’s 14 July 1947 speech to the opening session of the Conference on European Economic Cooperation, preserved in [Documents on Irish Foreign Policy, volume 8](https://www.difp.ie/volume-8/1947/speech-by-sean-lemass-to-the-opening-session-of-the-conference-on-european-economic-co-operation/4466/). `A1`, attribution and wording `high`, clearance `low/check`.

Voice guidance: practical economic sovereignty, productive capacity, trade, and chosen cooperation. Avoid treating Lemass as a simple free-trade spokesman. The often-repeated 1959 line about “the world trend ... towards freer trade” was encountered in a secondary educational source; it is a search lead until the primary Dáil passage is checked. Do not ship it as a Lemass quotation yet.

### William T. Cosgrave

Preferred security quote: “the fruit of the steady, persistent attack against the State and its fundamental institutions.” Source: [Oireachtas notable debate, assassination of Kevin O’Higgins, 1927](https://www.oireachtas.ie/en/debates/notable-debates/). A contemporary newspaper reproduction is also available in the [Dungarvan Observer, 16 July 1927](https://archive.waterfordcouncil.ie/Historical%20Newspapers%2C%20Books%20and%20Journals/Newspapers/Dungarvan%20Observer/1927/Dungarvan_Observer_07_July_16.pdf). `A1/B`, wording and attribution `high`, clearance `low/check`.

Voice guidance: public order, state continuity, institutional defence, and the cost of political violence. The quote is not an all-purpose Fine Gael motto; it belongs to a specific assassination and security context. A diplomatic alternative is Cosgrave’s 2 November 1930 speech about a “better understanding and a growing friendship” after former conflict, preserved in [DIFP volume 3](https://www.difp.ie/volume-3/1930/visit-of-hertzog-to-ireland/1169/).

### Richard Mulcahy

Preferred state-building fragment: “living our own lives in our own country, and developing our own resources.” Source: [Mulcahy’s Treaty debate, 22 December 1921](https://www.oireachtas.ie/en/debates/debate/dail/1921-12-22/2/). `A1`, wording and attribution `high`, clearance `low/check`.

Voice guidance: defence, civil administration, disciplined state-building, and material self-reliance. The full speech is a long Treaty argument; do not paste it into a focus or event. The 1931 unemployment debate is a usable policy lead, with Mulcahy referring to “grave economic perils” and the need for a “definite constructive policy”; use only after checking the exact excerpt in the [17 December 1931 Dáil record](https://www.oireachtas.ie/en/debates/debate/dail/1931-12-17/32/).

### John A. Costello

Preferred coalition/republic fragment: “This Bill burns no bridges leading either to national unity or to closer friendship with the people of our neighbouring country.” Source: [Costello’s Republic of Ireland Bill speech, 24 November 1948](https://www.oireachtas.ie/en/debates/debate/dail/1948-11-24/51/). `A1`, wording and attribution `high`, clearance `low/check`.

The legal title reference **Republic of Ireland Act 1948** is safer and more reusable than a long speech excerpt. Source: [Irish Statute Book, Republic of Ireland Act 1948](https://www.irishstatutebook.ie/eli/1948/act/22/enacted/en/html), enacted 1948 and brought into operation in 1949. Costello’s voice is legal, constitutional, conciliatory toward Britain while insisting on independent status. Do not make the Act appear to settle partition by itself.

### James Dillon

Preferred Civil War-memory fragment: “every decent Irish Nationalist wants to forget them and to work for the future.” Source: Dillon’s intervention in the [Army Pensions Bill debate, 27 October 1932](https://www.oireachtas.ie/en/debates/debate/dail/1932-10-27/22/). The same passage records his distress that the dispute damaged “the high name of this country.” `A1`, wording and attribution `high`, clearance `low/check`.

Voice guidance: outspoken nationalism, memory, reconciliation without erasure, and concern for the country’s reputation. Do not turn Dillon’s later pro-Allied stance into a generic 1936 starting position; use the relevant date and issue when the text is shown.

### William Norton

1. **Neutrality.** Norton told the Dáil in March 1939 that Ireland should tell Britain, Europe, and the world that it desired to preserve neutrality and would not enter entangling alliances. Source: [Army debate, 22 March 1939](https://www.oireachtas.ie/en/debates/debate/dail/1939-03-22/18/). A safe short fragment is “we desire to preserve our neutrality.” `A1`, confidence `high`, clearance `low/check`.
2. **Social policy.** Norton described asking a worker to support a family on 44 shillings a week as asking him to do what “every member of the Government knows is a physical impossibility.” Source: [Vote on Account, 14 March 1947](https://www.oireachtas.ie/en/debates/debate/dail/1947-03-14/4/). `A1`, confidence `high`, clearance `low/check`.
3. **Rural distress.** “the continued depression in the rural areas and the present suicidal drift from the land and the rural areas” is also preserved in the same 1947 debate. Use as a rural-Labour response only; it is too long and sharp for a generic button.

Voice guidance: parliamentary Labour, organised labour, wages, housing and social provision, while still defending neutrality. Do not collapse Norton’s Labour voice into Republican Congress revolutionary language.

## Party and movement material

### Labour and the Democratic Programme

**Selected historical text:** “the ownership of Ireland is vested in the people of Ireland.”  
Source: the [University of Galway Archives catalogue entry for a 1919 typescript copy of the Democratic Programme](https://archivesearch.library.universityofgalway.ie/index.php/typescript-copy-of-the-democratic-programme), which records that it was endorsed by Dáil Éireann and declared ownership vested in the people. A readable institutional reproduction is [Cork City Libraries’ First Dáil programme](https://www.corkcitylibraries.ie/media/llzjagk1/a_new_ireland_begins_the_first_dail.pdf); the [Labour Party’s historical page](https://labour.ie/news/2019/01/18/implementing-labours-democratic-programmes/) explains Labour’s continuing use of its social language. Date: 21 January 1919. Source tier `A2/B`; confidence `high` for the programme’s existence and core wording; clearance `check` for the reproduction, `low` for a short historical fragment with attribution.

Fit: useful for Labour, trade union, social republican, and worker/small-farmer surfaces. It is a First Dáil programme with Labour influence, not a 1936 Labour Party manifesto. Do not attribute every line to William Norton or Tom Johnson without checking the particular drafting history.

**Labour archive title:** *Labour’s Programme for a Better Ireland*, Labour Party general-election manifesto, 1943. Source: [National Library of Ireland catalogue](https://catalogue.nli.ie/Record/vtls000533911). This is a source title and provenance lead, not a cleared quotation: `A2`, confidence `high`, clearance `check` because the NLI record says copyright is owned by the National Library.

**Candidate/hold:** a 25 November 1948 Dáil speech contains the phrase “freedom from want, the economic freedom which alone makes political freedom real.” The searchable Oireachtas transcription places it in the Labour contribution, but the page’s long debate format makes the precise speaker heading worth checking before implementation. Source: [Republic of Ireland Bill debate, 25 November 1948](https://www.oireachtas.ie/en/debates/debate/dail/1948-11-25/27/). Use as `medium` attribution confidence until manually verified; do not present it as William Norton.

### Clann na Talmhan and rural producer politics

**Selected title reference:** *Clann na Talmhan* — literally “Family of the Land” in contemporary explanatory material. Source: [Irish Times account of the party’s 1939 foundation](https://www.irishtimes.com/opinion/letters/farmers-party-of-70-years-ago-1.794356); academic context: [Irish Political Studies, “On the Road to Extinction”](https://www.tandfonline.com/doi/full/10.1080/07907184.2010.518699) and [History Ireland](https://historyireland.com/clann-na-talmhan-irelands-last-farmers-party/). `B`, confidence `high`, clearance `low` for the party name.

**Candidate rural protest quote:** “Clann na Talmhan has not many landlords to drive ... but it has landlordism No. 2, namely, politicians, and they must go.” Michael Donnellan, 1942, Irish Farmers’ Paper, as quoted by the academic article above. `B`, confidence `medium/high` for the mediated wording and attribution, clearance `check`; use only the short fragment and retain the academic citation. The original newspaper scan was not obtained in this pass.

Fit: western small farmers, land reclamation, rates, roads, afforestation, co-operatives, and resistance to urban/departmental control. Do not use “Family of the Land” as an invented party slogan; it is a translation/explanatory title reference. Do not turn Clann into a generic fascist or socialist party: its agrarian programme and regional base must remain visible.

### IRA, Army Council, prisoners, and Civil War memory

**Selected archival statement fragment:** “The Irish Republican Army seeks to rally the mass of Irish people to take their stand again as free citizens of a United Irish Republic.” Source: the [UCD Elgin O’Rahilly Papers catalogue](https://www.ucd.ie/archives/t4media/p0200-orahilly-elgin-descriptive-catalogue.pdf), describing an Easter Sunday 1932 Army Council statement to be read at commemorations. `A2`, confidence `high` for the catalogue’s transcription and provenance, clearance `check` because the archive controls reproduction.

**Primary-title leads:** [NLI catalogue, Statement by Army Council, Easter 1933](https://sources.nli.ie/Record/MS_UR_003360); [Irish Republican Digital Archive, 1924–49 collection overview](https://republicanarchive.com/2026/01/12/the-twilight-years-1924-1949/); [Irish Republican Army, “To the Irish Race Everywhere,” 1938 scan](https://republicanarchive.com/wp-content/uploads/2025/11/to-the-irish-race-everywhere-1938.pdf). These are `A2`, high-confidence title/provenance leads. Use the title **Army Council**, **Óglaigh na hÉireann**, **United Irish Republic**, **commemoration**, **prisoners**, or **the Republic** only when the specific date and organisation are clear.

The [Military Archives Controller of Censorship collection](https://www.militaryarchives.ie/en/reading-room-collections/office-of-the-controller-of-censorship) confirms the state-side record of censorship from 1939–45 and is useful for the IRA/security countervoice. The IRA route must show violence, detention, executions, hunger strikes, informers, and public legitimacy costs; it must not romanticise an armed organisation merely by giving it heroic text.

### Republican Congress and the social-republican split

**Selected Athlone Manifesto candidate:** “We believe that a Republic of a united Ireland will never be achieved except through a struggle which uproots capitalism on its way.” Source: [An Phoblacht’s account of the Athlone Manifesto, 7–8 April 1934](https://www.anphoblacht.com/contents/19902), corroborated by the [University of Galway George Gilmore Papers catalogue](https://archivesearch.library.universityofgalway.ie/index.php/papers-of-george-gilmore) and the [Irish Republican Digital Archive glossary](https://republicanarchive.com/glossary-of-republican-organisations/). `B/A2`, confidence `high` for the manifesto’s existence and political meaning, `medium/high` for exact punctuation because the accessible wording is a later reproduction; clearance `check`.

**Backup:** the same manifesto is reported as describing the future republic as one of “the workers and small farmers.” Keep the source tied to the Athlone Manifesto; do not turn this into a general slogan for every IRA faction.

**Attribution warning:** “We cannot conceive of a free Ireland with a subject working class; we cannot conceive of a subject Ireland with a free working class” is repeatedly reproduced in left-republican material and associated with James Connolly and the Republican Congress. The accessible copies consulted did not provide a definitive primary edition for the exact wording and provenance. Treat it as `C/B`, confidence `medium`, clearance `check`, and **do not ship as a clean Connolly quotation until the original text or a scholarly edition is checked**. The safe alternative is the Athlone Manifesto sentence above with its explicit 1934 source.

The [George Gilmore archive](https://archivesearch.library.universityofgalway.ie/index.php/papers-of-george-gilmore) is especially useful for the route’s actual character: the Congress attempted to organise anti-imperialist activity across party affiliations, involved labour and Protestant workers, split over organisation and strategy, and dissolved by 1935. Use **United Irishmen** as a banner/title reference only where the 1934 Bodenstown context is intended; do not use “Protestant, Catholic and Dissenter” as a Republican Congress quote without a primary source.

### Eoin O’Duffy, corporatism, Spain, and succession

**Selected corporatist candidate:** “Only by this road can we advance to the new and better order, which we may call the corporative order.” Eoin O’Duffy, Fine Gael ardfheis speech, 9 February 1934, reproduced in the [Irish Times archive](https://www.irishtimes.com/opinion/february-9th-1934-1.460142). `B`, confidence `high` for the reproduced wording and attribution, clearance `check`; use only the short excerpt.

**Backup:** “to reform the abuses of private property, not to do away with it.” O’Duffy, 2 March 1935, reproduced in the [Irish Times archive](https://www.irishtimes.com/news/from-the-archives-march-2nd-1935-1.1316876). `B`, confidence `high`, clearance `check`.

**Title/source references:** **National Corporate Party**, **Irish Brigade**, **Spain**, and **corporative order**. Academic context is provided by the [Cambridge article on Fine Gael’s corporate labour policy in 1934](https://www.cambridge.org/core/journals/irish-historical-studies/article/corporate-labour-policy-of-fine-gael-1934/501EC92A694F9D47E2E03099430C859D) and the official diplomatic record [Eoin O’Duffy, DIFP volume 5](https://www.difp.ie/volume-5/1937/eoin-oduffy/2201/).

Fit: the voice is anti-parliamentary, corporatist, anti-communist, and leader-centred, with a distinct Spanish/Franco connection. It is not Fine Gael’s default voice. Any O’Duffy route must expose paramilitary coercion, fascist alignment, sectarian/exclusionary consequences, and political failure rather than presenting corporatism as neutral administrative efficiency.

**Rejected attribution:** “Christ and Antichrist” and similar short O’Duffy lines found in unsourced or encyclopedic retellings were not selected. No primary text was secured in this pass. Mark `C/reject` until a dated speech or pamphlet scan is available.

### Ailtirí na hAiséirghe, Gaelic authoritarianism, and antisemitism

**Archival programme/title references:**

- *For National Government and Action* and *Ireland’s Twentieth Century Destiny*, Gearóid Ó Cuinneagáin / Ailtirí network, 1942–43. Source: [UCD Ernest Blythe Papers descriptive catalogue](https://www.ucd.ie/archives/t4media/p0024-blythe-ernest-additional-descriptive-catalogue.pdf). `A2`, confidence `high` for titles and catalogue provenance, clearance `check`.
- “to make Ireland Free, Gaelic, in its social and economic systems the exemplary Christian state in our time.” The wording is preserved in the same UCD archival catalogue as a programme description. `A2`, confidence `high` for catalogue wording, `medium` for its relationship to the original pamphlet’s exact typography, clearance `check`; use as a short source-labelled fragment only after scan review.
- *Ireland: functional democracy — a Christian alternative to the servile state*, 1943. Source: [UCD Seosamh Ó Duibhginn Papers catalogue](https://www.ucd.ie/archives/t4media/p0172-oduibhginn-seosamh-descriptive-catalogue.pdf). Treat as a title reference, not a slogan generated by the game.
- [NLI catalogue, Aiséirghe, 1942](https://catalogue.nli.ie/Record/vtls000241252) confirms an original 60-page publication with English text in Irish. The catalogue is the provenance anchor for the pamphlet, not a clearance to reproduce its full contents.

Academic context: [History Ireland on Ailtirí’s fascist new order](https://historyireland.com/ailtiri-na-haiseirghe-irelands-fascist-new-order/) and [RTÉ Brainstorm on O’Duffy and Ailtirí](https://www.rte.ie/brainstorm/2024/1010/1474690-blueshirts-eoin-oduffy-ailtiri-na-haiseirghe-history-anti-immigration-protests/). These support the movement’s totalitarian, aggressively Gaelic, anti-democratic, and Christian-corporate character, but they are secondary sources.

**Antisemitism and attribution gap:** the [University of Galway study of Irish-language antisemitism](https://research.universityofgalway.ie/ws/portalfiles/portal/25885706/09-Dorothy%20N%C3%AD%20Uig%C3%ADn_0.pdf) specifically notes that there is no evidence that the author of a 1935 anti-Jewish letter signed “GEARÓID” was Gearóid Ó Cuinneagáin. Do not attribute that letter or any similar unsigned text to Ó Cuinneagáin. The feature may and should describe Ailtirí’s antisemitic/exclusionary politics where the route requires it, but use a named, dated, primary pamphlet or archival passage before displaying a direct antisemitic quote. `C/reject` for the uncertain letter.

### Clerical, producer, and Catholic social language

**Constitutional candidates:**

- “the welfare of the whole people” and “justice and charity shall inform all the institutions of the national life,” Article 45, Constitution of Ireland. Source: [Irish Statute Book Constitution](https://www.irishstatutebook.ie/eli/cons/en/html), with Article 45 wording also available through [the Constitution.ie text](https://theconstitution.ie/articles/45). `A1`, confidence `high`, clearance `low` for short legal fragments.
- “the special position of the Holy Catholic Apostolic and Roman Church,” original Article 44, 1937. Source: [Bunreacht 1937 Article 44 history](https://bunreacht1937.ie/article-44_religion/) and the [Cain reproduction of the original Constitution](https://cain.ulster.ac.uk/issues/politics/docs/coi37b.htm). `A1/B`, confidence `high`, clearance `low/check`. This special-position wording was removed in 1973; label it as historical 1937 language and do not present it as the current Constitution.
- **Rerum Novarum**, “Rights and Duties of Capital and Labor,” 1891. Source: [Vatican text](https://www.vatican.va/content/leo-xiii/en/encyclicals/documents/hf_l-xiii_enc_15051891_rerum-novarum.html). Use the title and section headings more readily than an excerpt. `A1`, confidence `high`, clearance `low/check` for a short historical reference.
- **Quadragesimo Anno**, 1931, “Reconstructing the Social Order.” Source: [Vatican text](https://www.vatican.va/content/pius-xi/en/encyclicals/documents/hf_p-xi_enc_19310515_quadragesimo-anno.html). Use as a source/title reference for producer, vocational, and anti-liberal-capitalist language; do not treat it as an Irish party manifesto.

**Attribution caution:** Seán MacEntee said in the 1937 Constitution debate that this was “the Constitution of a Catholic State.” Source: [Dáil Constitution debate, 11 May 1937](https://www.oireachtas.ie/en/debates/debate/dail/1937-05-11/29/). This is MacEntee’s political description, not the text’s legal declaration, and should be labelled accordingly. The original Constitution also named minority religious communities. Do not erase minority-faith language when representing clerical politics.

### Northern Ireland: unionist, nationalist, labour, industrial, local-government, and wartime language

**Unionist candidate, with correction:** “All I boast of is that we are a Protestant Parliament and a Protestant State.” This is the wording attributed to James Craig/Lord Craigavon in the 24 April 1934 Stormont debate. The [Northern Ireland Assembly official report](https://www.niassembly.gov.uk/globalassets/documents/official-reports/bound-volumes/may-2007-march-2011/bv58.pdf) reproduces and explicitly corrects the popular version. `B/official later reproduction`, confidence `high` for the corrected wording as reproduced and `medium` for direct primary verification in this pass, clearance `check`.

**Reject the common misquote:** “A Protestant Parliament for a Protestant People” is a later slogan/paraphrase associated with the controversy and later commentary; it should not be shipped as Craigavon’s verbatim 1934 wording. Source for the correction: the Assembly report above and the [UK Parliament research briefing](https://researchbriefings.files.parliament.uk/documents/CBP-8884/CBP-8884.pdf).

**Nationalist candidate/source lead:** Cahir Healy’s [Westminster Hansard profile](https://api.parliament.uk/historic-hansard/people/mr-cahir-healy/index.html) confirms his Fermanagh and Tyrone representation in the 1930s; the [1941 detention debate](https://api.parliament.uk/historic-hansard/commons/1941/sep/11/mr-cahir-healy-detention) documents the wartime detention of a Northern Ireland parliamentarian. No short Healy quotation was selected because the accessible records in this pass did not give a clean, dated primary passage whose wording and feature fit were both superior to the institutional references. Use **Cahir Healy**, **Fermanagh and Tyrone**, **Stormont**, **nationalist abstention**, and **detention** as source-labelled references, not invented slogans.

**Labour/industrial references:** **Belfast Outdoor Relief Strike (1932)**, **Harland and Wolff**, **Short and Harland**, **shipyards**, **engineering**, **industrial disputes**, and **working-class Protestant and Catholic labour** are safer title-like references than a generic “Northern workers” line. Use the [Northern Ireland War Memorial account of wartime industrial production](https://www.niwarmemorial.org/collections/blog/the-war-for-industrial-production), the [impact of the Belfast raids](https://www.niwarmemorial.org/impact-of-the-raids), and the [CAIN discrimination archive](https://cain.ulster.ac.uk/issues/discrimination/whyte.htm). These are `A2/B`, high confidence for the institutional context, but no direct quote should be presented without a specific primary page.

**Wartime references:** **Belfast Blitz**, **Easter Tuesday Raid**, **the Six Counties**, **Northern conscription**, and **US troops in Northern Ireland** are attested event/title references. The strongest official text lead is the [DIFP instruction on the deployment of United States troops in Northern Ireland](https://www.difp.ie/volume-7/1942/deployment-of-united-states-troops-in-northern-ireland-instructions-on-how-to-respond/3604/), which records Irish diplomatic concern and the pledge that Irish territory would not be used against Britain. Use **the Six Counties** only where the speaker or source is clearly republican/nationalist; use **Northern Ireland** or **Stormont** for neutral institutional narration.

### Constitution, neutrality, emergency law, censorship, and weather

**Neutrality candidate:** “The aim of the government policy is to maintain and preserve our neutrality in the event of war.” Source: [DIFP, Irish neutrality, 17 February 1939](https://www.difp.ie/volume-5/1939/irish-neutrality/2420/). This is a primary diplomatic document, `A1`, confidence `high`, clearance `low/check`. Fit: a clean state doctrine line for a focus, decision, or event response.

**Defence-of-neutrality candidate:** the same DIFP document says the state must be able to defend itself so that no one can attack or violate its territory with impunity. Use a short fragment only after checking the exact display length. Fit: coastwatch, Treaty Ports, military readiness, and foreign pressure.

**Emergency law candidate:** the [Emergency Powers Act 1939, section 2](https://www.irishstatutebook.ie/eli/1939/act/28/section/2/enacted/en/html) authorises orders for public safety, preservation of the State, maintenance of public order, and provision/control of supplies and services. The title and the short statutory list are `A1`, high confidence, `low` clearance for short legal use.

**Censorship candidate:** the [Military Archives Controller of Censorship collection](https://www.militaryarchives.ie/en/reading-room-collections/office-of-the-controller-of-censorship) preserves the statutory wording “censorship, restriction, control, or partial or complete suspension of communication.” `A2/A1`, high confidence, `check` clearance. Use this language to show the power and its cost; do not write censorship as consequence-free neutrality.

**Technical cooperation:** [DIFP on meteorological cooperation with Britain](https://www.difp.ie/volume-6/1940/metrological-co-operation-with-britain/3312/) and [DIFP on continued cooperation in 1944](https://www.difp.ie/volume-7/1944/co-operation-with-the-british-government/3785/) support **weather reports**, **Blacksod**, and **covert technical liaison** as title-like references. The [RTÉ 1940s archive](https://www.rte.ie/archives/exhibitions/681-history-of-rte/684-rte-1940s/289512-rte-1940s/) confirms wartime restrictions on weather broadcasting. Use the institutional titles rather than an invented coastwatch slogan.

### High Kingship, Five Provinces, royal sites, and Brehon material

**Selected title references:** **Lebor na Cert / The Book of Rights**, **the rights of the king of Tara**, **Ard Rí**, **Uisneach**, **Tara**, **Emain Macha**, **Dún Ailinne**, **Cashel**, and **Rathcroghan**.

Sources:

- [CELT, *Lebor na Cert* / *The Book of Rights*](https://celt.ucc.ie/document/T102900), an unknown-author medieval text in an English edition associated with Myles Dillon. Its section title “The rights of the king of Tara” is a safe title-like reference. The CELT edition states that the printed edition is controlled by the Irish Texts Society and is available with prior consent for research and teaching; use title-only or obtain permission for longer translated excerpts. `A2`, confidence `high` for title/provenance, clearance `restricted/check` for the translation.
- [Royal Sites of Ireland](https://royalsites.ie/about), an official heritage presentation of Tara, Uisneach, the four provincial royal sites, and the historical association with high kingship. `A2`, confidence `high` for site names/context, `check` for verbatim website wording.
- [CELT, *The History of Ireland*, section on the five provinces and Uisneach](https://celt.ucc.ie/published/T100054/text012.html). Use as a historical-literary source, not as proof that a single central High Kingship governed Ireland continuously. `A2`, confidence `medium/high`, clearance `check` for translation.
- [Monumental Ireland on the six royal sites and the debated fifth province](https://monumentalireland.ie/royal-sites/). It explicitly notes that Meath as a fifth province is debated. `B`, confidence `high` for the caution; use **five provinces** as historical/mythic framing, not an uncomplicated administrative fact.

**Brehon/legal material:** the [National Library of Ireland manuscript catalogue](https://sources.nli.ie/Record/MS_UR_075989) records Brehon-law tracts including *Seanchas Mór*. The [UCC CELT overview](https://www.ucc.ie/en/research-sites/celt/) explains that CELT contains historical Irish law and literature. Use **Seanchas Mór**, **Brehon law**, **fenechas**, **rights**, **custom**, **judgement**, and **stewardship** as source-labelled terms. Do not invent a one-line “Brehon principle” or claim that the medieval law tracts were a modern democratic constitution.

### Gaelic revival, heroic cycle, folklore, and regional Ireland

**Heroic-cycle references:** **Táin Bó Cúalnge / The Cattle-Raid of Cooley**, **Cú Chulainn**, **Sétanta**, **Emain Macha**, **Medb**, and **the Ulster Cycle**. The [UCC Irish Sagas Online extract](https://iso.ucc.ie/Tain-cualnge/Tain-cualnge-4-text.pdf) provides the original, modern Irish, and English translation for the youthful deeds of Cú Chulainn. It is a scholarly translation with use restrictions; use titles and names, or clear a very short excerpt. `A2`, confidence `high`, clearance `check/restricted` for translated prose.

**Revival references:** **Gaelic League**, **Gaelic Athletic Association**, **National Literary Society**, **Irish Literary Revival**, **Abbey Theatre**, **Yeats**, **Lady Gregory**, and **Douglas Hyde**. The [NLI 1916 culture exhibition](https://www.nli.ie/1916/exhibition/en/content/stagesetters/culture/) and [NLI Yeats material](https://www.nli.ie/learn/downloadable-resource-irish-folklore-and-fairy-tales-work-wb-yeats) are suitable provenance anchors. Use **The Celtic Twilight** as the selected allusion, not an invented “Gaelic soul” slogan.

**Regional references:** the [Logainm Placenames Database](https://www.logainm.ie/en/) and its [Government open-data record](https://data.gov.ie/dataset/logainm) support Irish/English place-name pairing, townlands, regional terms, and local cultural work. The [National Folklore Collection overview](https://www.duchas.ie/en/info/cbe) and [Schools’ Collection description](https://www.duchas.ie/en/info/cbe-collections) document material collected across the island, including local legends, oral literature, historical tradition, and place-name lore. The [National Monuments Service Historic Environment Viewer](https://www.archaeology.ie/advice-and-support/locate-a-monument-or-wreck/historic-environment-viewer/) supports site and monument references without turning archaeology into supernatural proof.

Use regions as lived, named places: Connacht, Leinster, Munster, Ulster, Mide/Meath, Dublin, Belfast, the western counties, the Border counties, and the Gaeltacht. Avoid treating “the West,” “Ulster,” or “the rural Irish” as one voice. Attach a source, informant, office-holder, party, county, or institution to a regional line where possible.

## Cultural and remark candidate comparison

| Candidate | Provenance | Fit | Status/clearance |
| --- | --- | --- | --- |
| *The Celtic Twilight* | W. B. Yeats, 1893; Project Gutenberg and NLI context. | Serious revival/folklore/Otherworld allusion; title-like, not a state slogan. | **Selected.** `A2/B`, high, `low` title use; check territory for longer text. |
| “There is a fort at the back of our garden in Fairymount.” | Dúchas Schools’ Collection, Roscommon, 1937–39. | Evidence/testimony, regional Otherworld investigation, local voice. | **Recommended evidence backup.** `A2`, wording high, speaker medium, `low/check` under CC BY page terms. |
| *Lebor na Cert / The Book of Rights* | Medieval Irish legal/royal text, CELT edition. | High Kingship, rights, tribute, provincial order. | Title-only preferred; translated excerpts `restricted/check`. |
| *Táin Bó Cúalnge* | Medieval saga; UCC Irish Sagas Online scholarly edition. | Heroic duty, obligation, province, exceptional violence. | Title/name references preferred; translation `check/restricted`. |
| *Aiséirghe* / *Ireland’s Twentieth Century Destiny* | Ailtirí publications in NLI/UCD catalogues. | Gaelic authoritarian cultural capture. | Backup for the Ailtirí route; title/short archive fragment `check`; no softening of exclusionary ideology. |
| *Clann na Talmhan* / “Family of the Land” | Contemporary party name and historical accounts. | Rural producer politics and western smallholder identity. | Safe title reference; do not present translation as an attested slogan. |
| “The Ireland That We Dreamed Of” | De Valera’s 1943 broadcast title/phrase in RTÉ archive. | Strong cultural-state vision. | **Do not select for direct display.** RTÉ says reproduction requires licensing; title-only `restricted`. |
| “A Protestant Parliament for a Protestant People” | Later slogan/paraphrase associated with Craigavon controversy. | Northern sectarian rhetoric. | **Reject as Craigavon direct quote.** Use corrected 1934 wording if needed, with source caveat. |

## Route, focus, decision, and event localisation mapping

The main agent should map these working package labels to the actual implementation keys. No unrevealed route names or guessed focus IDs are supplied here.

| Package / voice | Focus and route localisation surfaces | Decision/event localisation surfaces | Dynamic context to expose |
| --- | --- | --- | --- |
| Constitutional drafting, Dáil, Seanad, Presidency, coalition | Constitutional settlement focus title/description; Dáil and Seanad institutional tooltips; presidential office text; coalition-building focus descriptions. Use the selected Article 1 fragment on the constitutional surface. | Constitution referendum, office-holder change, coalition formation, Seanad/Dáil procedure, Republic Act lifecycle. | Office-holder, chamber, bill/law, vote result, coalition composition, territorial claim. |
| Neutrality, Emergency law, censorship, internment, weather | Neutrality doctrine, Treaty Ports, coastwatch, emergency administration, weather liaison, and “defend freedom of action” focuses. | Foreign aircraft/vessel incident, censorship order, internment decision, weather-report exchange, port violation, diplomatic protest. | Incident type, belligerent, legal authority, port/sector, public legitimacy, exposure, technical sponsor. |
| Labour, unions, housing, wages, transport | Labour settlement, wage policy, housing, transport, public works, and trade-union negotiation descriptions. Use Norton and Democratic Programme material in separate voices. | Wage dispute, strike, housing queue, supply crisis, transport stoppage, Labour confidence/coalition event. | Wage band, household burden, union, sector, county/city, party spokesperson, provision level. |
| Clann na Talmhan and rural producer politics | Smallholder, rates, reclamation, roads, co-operative, afforestation, and county agricultural focus text. Use *Clann na Talmhan* as a source/title reference, not an invented slogan. | Tillage quota, land seizure, dairy/price dispute, rural road/co-op decision, western farmer rally. | County, farm size/value band, crop/livestock, co-op sponsor, local official, enforcement intensity. |
| IRA / Army Council / prisoners / Civil War memory | Security, prisoner, Army Council, commemoration, partition, and state legitimacy descriptions. Avoid heroic generic republicanism. | Arms discovery, prison hunger strike, execution/interment, IRA statement, Civil War memory/reconciliation event. | Organisation/faction, prisoner status, county, incident severity, security response, public consent. |
| Republican Congress / anti-sectarian social republicanism | Workers-and-small-farmers, anti-fascist, common programme, northern labour, and Protestant/Catholic/Dissenter outreach descriptions. Use the Athlone Manifesto only with its date. | Athlone-style congress, faction split, workers’ rally, Belfast outreach, Spanish veterans, programme vote. | Faction, class coalition, religious/community participation, region, foreign war experience, organisational form. |
| O’Duffy / National Corporate Party / Spain | Corporative order, National Corporate Party, Spanish brigade, leader succession, and anti-parliamentary crisis text. Do not use Fine Gael as a synonym for O’Duffy. | Paramilitary rally, Spanish returnees, corporate council proposal, clerical/business response, succession crisis. | Leader, party, organisation, clergy/business sponsor, paramilitary activity, coercion, foreign alignment. |
| Ailtirí / Irish-language total state | Irish-language cultural institution and coercive Ailtirí route text must be separated. Use archival titles and state the authoritarian/exclusionary stakes. | Publication seizure, language enforcement, party split, antisemitic/exclusionary policy consequence, resistance, foreign-fascist contact. | Publication, language domain, coercive level, target community, party faction, archive evidence, public backlash. |
| Clerical / producer / Catholic social thought | Article 44 historical religious settlement, Article 45 social order, vocational/producer councils, minority-faith guarantees, Vatican diplomacy. | Church intervention, Catholic social policy, school/hospital dispute, Vatican note, minority-faith protection or exclusion. | Article/date, denomination, institution, sponsor, social group, legal status, clerical pressure. |
| Northern Ireland | Stormont, unionist, nationalist, Northern Labour, Belfast industry, local-government, and Border terminology; correct Craigavon wording only. | Belfast Blitz/relief, Northern conscription, Healy detention, local council, cross-border labour/industry, 1940 unity proposal, US troops. | Province/county/city, unionist/nationalist/labour consent, industry, local authority, British flexibility, security stability. |
| Gaelic revival / High Kingship / Five Provinces / regional culture | Gaelic League/GAA/literary revival, royal sites, provincial institutions, Brehon archive, folklore collection, and place-name work. | Site survey, archive acquisition, provincial gathering, cultural funding, language school, local collector testimony. | Region, site, language, archive/source tier, institution, local informant, cultural integration stage. |
| Otherworld / impossible route framing | Hidden evidence and consequence text only after testimony, site, archive, or obligation has been established. Use *The Celtic Twilight* and Dúchas terms as allusions, never as unexplained route branding. | Folklore testimony, damaged fairy fort, impossible weather/site incident, obligation/debt, false lead, reveal, consequence. | Region, informant, evidence type, credibility, incident severity, obligation, investigation stage, integration/acceptance stage. |

## Terminology and tone guidance

- Use **Éire**, **Ireland**, **Saorstát Éireann**, **the Republic**, **the Twenty-Six Counties**, **the Six Counties**, **Northern Ireland**, **Stormont**, and **the Border** according to the speaker, date, and institution. Do not use them interchangeably in neutral narration.
- **Ard Rí**, **Tara**, **Uisneach**, **Mide**, and the provincial royal sites are historical, literary, and ceremonial references. They do not prove a continuous central monarchy or justify modern annexation.
- **Cúige / Five Provinces** should be framed as historical and mythic language with a debated fifth province, not as a fixed 1936 administrative map.
- **Brehon law**, **Senchas Mór**, and **fenechas** are source terms. Avoid modern “natural law,” “democracy,” or “socialism” claims unless a dated modern speaker is making the analogy.
- **Producer**, **vocational**, **corporative**, **Catholic social**, **Gaelic**, **republican**, **Labour**, and **neutrality** are not interchangeable. Attach each to its institutional or political advocate.
- Ailtirí’s Gaelic language policy can share vocabulary with legitimate revival work while its totalitarian, antisemitic, coercive, and exclusionary politics remain explicit. Do not romanticise the route through poetic language alone.
- O’Duffy’s corporatism, IRA violence, emergency internment, censorship, executions, and Northern sectarianism must retain consequences and affected communities in the text.
- Hidden Otherworld text should begin with evidence, testimony, place, damage, weather, obligation, or a disputed archive entry. Do not announce an “Otherworld route” in visible text.
- Avoid direct modern copyrighted song, film, radio, or broadcast prose. Short historical fragments, titles, statutes, archival phrases, and public-domain literary titles are the preferred surfaces.

## Gaps, uncertain candidates, and rejected material

1. A primary scan of the 1934 Athlone Manifesto was not secured. The An Phoblacht reproduction and University of Galway archive provide a strong provenance trail, but exact punctuation and edition rights remain `check`.
2. The commonly repeated Connolly/Republican Congress line about a free Ireland and a subject working class has not been assigned a definitive primary edition in this pass. Do not ship it as a clean quotation until checked.
3. The exact 1934 Stormont primary page for Craigavon’s wording was not directly accessed. The Northern Ireland Assembly official report gives the corrected wording and explicitly identifies the popular version as a misquotation. Use the corrected form only with that caveat; reject the popular form.
4. A clean, short primary quotation from Cahir Healy, the Northern Ireland Labour Party, or a 1930s Northern local council was not selected. Use institutional titles and archival references until a specific Stormont or council record is verified.
5. A searchable 1948 Labour phrase about “freedom from want” needs speaker-heading verification before being attributed to a named Labour TD. It is a research lead, not a selected quote.
6. Ailtirí’s antisemitic material requires a named, dated primary pamphlet or archive scan. The University of Galway study warns against attributing an unsigned “GEARÓID” letter to Ó Cuinneagáin. Do not fill this gap with a quote-site line.
7. Translated CELT editions of *Lebor na Cert* and the *Táin* have edition-specific permissions. Use names/titles or obtain clearance for longer translated text.
8. RTÉ’s de Valera broadcast archive is real and culturally valuable, but its page states that reproduction requires licensing. Use the broadcast title as an allusion only unless permission is obtained.
9. No audio selection is made. The prompt’s optional coastwatch ambience, constitutional ceremony, and verified Otherworld cue remain independent of this text handoff; no route or achievement should depend on audio.

## Short implementation recommendation

Use the selected Article 1 fragment as the main constitutional/civic quote, the *Celtic Twilight* title as the selected cultural allusion, and the Dúchas Fairymount sentence as the evidence-first Otherworld backup. Use leader-specific fragments only on dated or institution-specific surfaces. Keep every direct excerpt short, attach provenance in the research record, preserve the `high/medium/uncertain` attribution labels above, and route all `check/restricted` candidates through a final rights review before adding them to localisation.

The main agent should not invent a single national slogan to cover all twelve packages. The strongest package is a layered text system: constitutional law for the state, parliamentary and diplomatic records for the leaders, manifestos and party names for movements, archival testimony for regional culture, and carefully labelled literary/folkloric titles for the impossible route.
