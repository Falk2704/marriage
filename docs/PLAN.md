# Implementation Plan

Wedding website for Isabell & Falk. 29 August 2026. Hotel Freihof Prichsenstadt.

---

## Technical Decisions

| Component       | Choice                                    |
| --------------- | ----------------------------------------- |
| Markup          | Plain HTML (single `index.html`)          |
| Styling         | Tailwind CSS via CLI (built to `dist/`)   |
| Fonts           | Google Fonts: PT Serif, Petit Formal Script |
| Build           | Tailwind CLI only                         |
| Deploy          | GitHub Pages via GitHub Actions           |
| Language        | German only                               |
| Client-side JS  | None                                      |

---

## Repository Structure

```
marriage/
├── website/
│   ├── index.html              # Single-page site (all sections)
│   ├── src/
│   │   └── input.css           # Tailwind directives
│   ├── dist/
│   │   └── output.css          # Built CSS (gitignored)
│   ├── tailwind.config.js      # Custom colors, fonts, spacing
│   └── package.json            # Only dependency: tailwindcss
├── assets/                     # Images, .ics file
├── scripts/                    # Python tooling
├── docs/                       # Planning and design docs
└── .github/
    └── workflows/
        └── deploy.yml          # GitHub Pages deployment
```

---

## Page Sections (top to bottom)

| # | Section                  | ID              | Background | Content Status       |
|---|--------------------------|-----------------|------------|----------------------|
| 1 | Navigation               | (sticky)        | transparent / bg on scroll | New |
| 2 | Hero / Welcome           | `#hero`         | `bg`       | Real content         |
| 3 | Event Details            | `#details`      | `bg-alt`   | Partial placeholder (time TBD) |
| 4 | Schedule / Ablauf        | `#ablauf`       | `bg`       | Placeholder structure |
| 5 | Travel / Anreise         | `#anreise`      | `bg-alt`   | Real content + map   |
| 6 | Accommodation / Unterkunft | `#unterkunft` | `bg`       | Placeholder structure |
| 7 | Gifts / Wuensche         | `#wuensche`     | `bg-alt`   | Real content         |
| 8 | Footer                   | `#footer`       | `bg`       | Real content         |

### Section Details

**Navigation**: Sticky bar with anchor links to each section. PT Serif all-caps with wide tracking. Smooth scroll via CSS `scroll-behavior: smooth`.

**Hero**: Central focal point. "Isabell & Falk" in Petit Formal Script. Date in PT Serif all-caps with wide spacing ("29 . AUGUST . 2026"). Venue name. Main architectural line-art illustration (gatehouse/arch SVG).

**Event Details**: Venue full name and address. Date. Time placeholder.

**Schedule**: Visual timeline layout. Placeholder entries: Ceremony, Reception, Dinner, Party. Times to be filled in.

**Travel**: Directions by car and train. Existing map image (`hochzeit_map.png`). Google Maps link/embed for Hotel Freihof Prichsenstadt.

**Accommodation**: Card/list layout for hotel recommendations. Structure: name, address, link, notes. Content to be filled in.

**Gifts**: Direct but warm German text communicating that monetary gifts are appreciated. No bank details or PayPal.

**Footer**: "Isabell & Falk . 29.08.2026". Small architectural motif.

---

## Decorative Elements

- One main architectural SVG illustration in the hero (gatehouse/arch motif)
- Simplified monoline line-art dividers between sections
- All decorative elements in primary green (`#4F6F5B`)
- Thin, consistent stroke weight
- Symmetric, controlled, no fills or gradients

---

## Implementation Backlog

| # | Task                        | Acceptance Criteria                                                |
|---|-----------------------------|--------------------------------------------------------------------|
| 1 | Set up Tailwind CLI         | `package.json` in `website/`, `npm run build` and `npm run dev` work |
| 2 | Configure Tailwind          | Custom colors, fonts, spacing in `tailwind.config.js`              |
| 3 | HTML structure              | All 7 sections with semantic HTML and anchor IDs                   |
| 4 | Hero section                | Names, date, venue styled per design constitution                  |
| 5 | Event details section       | Venue info, address, date visible                                  |
| 6 | Schedule section            | Timeline layout with placeholder entries                           |
| 7 | Travel section              | Directions, map image, Google Maps link                            |
| 8 | Accommodation section       | Card layout with placeholder structure                             |
| 9 | Gifts section               | German text, warm and direct tone                                  |
| 10 | Navigation + footer        | Sticky nav, anchor links, smooth scroll, footer                    |
| 11 | SVG line art               | Hero illustration + section dividers                               |
| 12 | Responsive polish          | Mobile-first, tested at common breakpoints                         |
| 13 | GitHub Pages deployment    | Actions workflow builds CSS, deploys `website/`                    |

---

## Deferred Items

| Item                  | Reason                                              |
|-----------------------|-----------------------------------------------------|
| RSVP                  | Mechanism and storage TBD                           |
| Password protection   | Requires server-side solution (client-side rejected)|
| Photo gallery         | Add when photos are ready                           |
| Custom domain         | Can be added to GitHub Pages later                  |
| FAQ                   | Not selected                                        |
| Contact               | Not selected                                        |

---

## Content Placeholders

These sections have the structure built but need real content from the couple:

- **Schedule times**: Ceremony, reception, dinner, party times
- **Accommodation**: Hotel names, addresses, links, notes
- **Event details**: Exact start time
