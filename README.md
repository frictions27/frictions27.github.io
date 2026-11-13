# Frictions

The GitHub Pages site for the Frictions 2027 Symposium, built with Jekyll.

The symposium takes place Monday–Friday, 1–5 March 2027. The schedule is a
preview: session times and event details are placeholders.
Edit the files in `_events/` to update the programme. Each event's front matter
sets its title, category, day, display time, calendar slot and length (in hours),
venue (with an optional `map_url` Google Maps link, shown as a 📍 pin), session organizer, speakers, participants and respondents. Enter people
as YAML lists; empty fields are hidden on the event page. For example `speakers: [Name One, Name Two]`. Write the abstract
in the Markdown body below the front matter. The event detail page renders these
fields from the same file. Use `title_es`, `category_es`, `venue_es`,
`session_organizer_es`, and `abstract_es` for Spanish translations where
applicable; write the English abstract in the Markdown body and the Spanish
abstract as Markdown in `abstract_es`. Set `slot` to the event's start hour in 24-hour time
(for example, `9` for 09:00 or `13` for 13:00 / 1 p.m.). The calendar shows
10:00–19:00, so events are clipped to those visible hours. `length` is the event's
duration in hours. Replace the conference abstract on the home page when it is
ready. The home page currently uses linked text placeholders for supporter
logos; replace them with approved logo files when available.

The call pages are placeholders; edit the files under `calls/` when the call
details are ready. The landing-page background can be changed using the
`--hero-background` CSS variable; the previous green is `var(--accent)`.

To add a participant, create a Markdown file in `_participants/`, for example
`_participants/jane-example.md`:

```markdown
---
title: Jane Example
function: Co-organizer
function_es: Coorganizadora
image: /assets/images/jane-example.jpg
bio_es: Una breve biografía en español.
links:
  - label: Website
    label_es: Sitio web
    url: https://example.com/
---
A short biography goes here. Markdown formatting is supported.
```

Upload the photograph at the specified path. The image and links are optional;
without an image a placeholder circle is shown. Add `function` and
`function_es` to show the participant's role under their name, and `bio_es`
for the Spanish biography (Markdown is supported). Each file automatically
appears on the Participants page and has its own profile page.

The site displays English and Spanish together rather than using a language
switch. Keep translations alongside the English when editing pages: call pages
use `title_es` and `content_es`; participant and event fields are described
above. Existing Spanish copy should be reviewed by the organizers.

Reading lists are Markdown files in `_reading_lists/`. Each appears on the
reading-lists page and can contain a bibliography as ordinary Markdown in its
body, with a Spanish version in `content_es` if needed. Set `title` and
`title_es` in the front matter. An event and a reading list link to each other
automatically only when their filenames match exactly, including case (for
example `_events/Engels.md` and `_reading_lists/Engels.md`). The five existing
lists are placeholders, not actual bibliographies.

To preview the site locally, install Jekyll and run `jekyll serve` from the
repository root. GitHub Pages builds the site from the repository.
