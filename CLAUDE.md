# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

```
marriage/
├── website/          # Static wedding website (Tailwind CSS)
│   ├── index.html    # Single-page site (German language)
│   ├── src/input.css # Tailwind source CSS
│   ├── dist/         # Built CSS output (generated, do not edit)
│   ├── images/       # PNG/illustration assets
│   └── tailwind.config.js
├── assets/           # savethedate.ics calendar file
├── scripts/          # Python utilities (QR code generation via uv)
├── docs/
│   ├── DESIGN_TOKENS.md  # Authoritative design values (colors, type, spacing)
│   ├── DESIGN.md         # Design principles and aesthetic rules
│   ├── PLAN.md           # Implementation plan and backlog
│   └── TASKS.md          # Prioritized task list
└── AGENTS.md         # Behavioral guidelines for agentic work
```

## Commands

### Website

```bash
# Development (watch mode)
cd website && npm run dev

# Production build
cd website && npm run build
```

### Scripts (Python/uv)

```bash
cd scripts && uv run main.py
```

## Design System

All visual decisions are governed by `docs/DESIGN_TOKENS.md` (authoritative) and `docs/DESIGN.md` (principles). Read both before any UI work.

**Color tokens** (defined in `tailwind.config.js`):

- `primary` (#4A6856) — all text, headings, nav, dividers
- `bg` (#F4F1E8) — page background (warm ivory)
- `bg-alt` (#E9E4D6) — alternating section backgrounds
- `accent` (#456650) — hover/focus states only
- `body` (#2F3A33) — long-form body text (use sparingly)

**Typography**: PT Serif (serif) + Petit Formal Script (script) via Google Fonts. Mobile-first responsive type scale in `DESIGN_TOKENS.md`.

**Layout**: `max-w-content` = 52rem, centered. Mobile/desktop breakpoints at `sm:` (640px) and `lg:` (1024px).

## Architecture

Single-page static site (`index.html`) with sections: hero, details, timeline (Ablauf), travel (Anreise), accommodation (Unterkunft), wishes (Wünsche). No JavaScript, no build framework beyond Tailwind CSS v3. Hosted on GitHub Pages.

Sections alternate `bg` / `bg-alt` backgrounds. Nav is sticky with smooth-scroll anchor links. `scroll-margin-top` is set in `src/input.css` to compensate for the sticky nav.

## Behavioral Guidelines

See `AGENTS.md` for detailed guidelines. Key points:

- Read design docs before any visual/UI change
- Do not introduce colors, fonts, or spacing not in the design tokens
- Keep changes minimal and targeted — no speculative additions
- Browser snapshot tool (`MCP_DOCKER_browser_snapshot`) returns accessible DOM; screenshots are not supported
