# Tasks

Prioritized task list derived from the UI/UX and design analysis. Grouped by urgency.

---

## P0 — Fix before sharing with guests

These are blockers. The site will look broken or produce a poor first impression if shared in this state.

- [x] **Fix broken images** — `celebration.png` and `clock.png` are corrupt (null bytes, need re-export from source). `hochzeit_map.png` is valid. Verified file headers.
- [x] **Add `scroll-margin-top` to all sections** — Added 5.5rem (mobile) / 3.5rem (desktop) via `input.css`. Verified heading is visible after nav-link scroll.
- [x] **Add social sharing meta tags** — Added `description`, `og:title`, `og:description`, `og:type`, `og:image`, `theme-color`, and inline SVG favicon to `<head>`.
- [x] **Fix `accent` hover color contrast** — Changed accent from `#6F8F78` to `#456650`. Now 5.69:1 on `bg`, 5.06:1 on `bg-alt` — both pass WCAG AA. Updated `tailwind.config.js` and `DESIGN_TOKENS.md`.

---

## P1 — Should fix

Meaningful quality and standards issues. Not visually broken, but degrade the experience.

- [ ] **Add `loading="lazy"` to below-fold images** — 0 of 12 images use lazy loading. All images below the hero (section icons, timeline icons, map, accommodation icon, globe) should have `loading="lazy"`.
- [ ] **Add explicit `width` and `height` attributes to images** — No `<img>` tags declare dimensions. This causes layout shift (CLS) as images load. Add `width`/`height` matching the intended display size.
- [ ] **Increase nav link tap targets on mobile** — Nav links render at 12px height on mobile. Minimum recommended tap target is 48px. Add vertical padding to nav links.
- [ ] **Add focus-visible styles** — The design constitution requires focus states using the `accent` color. Currently relies on browser defaults, which are inconsistent and often invisible on cream backgrounds. Add `focus-visible` outline styles to all interactive elements.
- [ ] **Remove unused font weights from Google Fonts import** — The import loads PT Serif 400, 700, and italic 400. Bold (700) and italic (400i) are never used on the page. Trim to only `wght@0,400`.
- [ ] **Remove `italic` from "Zeiten sind vorlaufig"** — `index.html:191` uses the `italic` class. The design constitution states: "No italic for emphasis." Use normal weight or adjust sizing/spacing instead.

---

## P2 — Improvements

Design constitution conformance and UX enhancements. Not urgent but raise quality.

- [ ] **Convert PNG illustrations to inline SVGs** — The design constitution requires "SVG format, inline" for all illustrations. All 12 images are raster PNGs. SVGs would be sharper on Retina, smaller in file size, and allow CSS color control. Priority: hero illustration first, then section icons.
- [ ] **Add train directions** — The Anreise section only covers car travel. A `travelbytrain.png` image exists in `website/images/` but isn't used. PLAN.md specifies "Directions by car and train."
- [ ] **Link the save-the-date calendar file** — `assets/savethedate.ics` exists but isn't linked anywhere on the page. Add a "Save to Calendar" link in the Details or Hero section.
- [ ] **Add `<header>` semantic wrapper** — The `<nav>` sits outside `<main>` without a `<header>` parent. Wrap `<nav>` in `<header>` for proper document semantics.
- [ ] **Visually distinguish primary accommodation** — Hotel Freihof (where the couple reserved a room block) looks identical to the other three options. Give it visual priority — a brief "Empfohlen" label, slightly different spacing, or positioning emphasis.
- [ ] **Reduce hero illustration to spec size** — The design constitution specifies 300–400px (desktop) / 200–280px (mobile). Current implementation is `w-[600px] lg:w-[700px]`, nearly double the spec.
- [ ] **Make subheading sizes responsive** — Subheadings (e.g., "Hotel Freihof", "Mit dem Auto") use `text-[1.125rem]` at all breakpoints. The type scale specifies 1rem on mobile, 1.125rem on desktop.
- [ ] **Fix `primary` on `bg-alt` contrast** — 4.40:1 narrowly fails WCAG AA for normal text (needs 4.5:1). Headings pass as large text, but small text like dividers and nav links on `bg-alt` sections technically fail. Consider darkening `primary` slightly or lightening `bg-alt`.

---

## P3 — Future features

Deferred items from PLAN.md. Not in current scope but documented for planning.

- [ ] **RSVP mechanism** — The primary interactive feature guests expect. Mechanism and storage TBD.
- [ ] **Contact information** — No way for guests to reach the couple from the site with questions.
- [ ] **Password protection** — Requires server-side solution (client-side rejected).
- [ ] **Custom domain** — Can be added to GitHub Pages later.
- [ ] **Photo gallery** — Add when photos are ready.
