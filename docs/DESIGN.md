# Design Constitution

Binding design principles for the Isabell & Falk wedding website. All implementation decisions must conform to this document. When in doubt, refer back to these rules.

Derived from the save-the-date card design.

---

## Aesthetic Identity

**Minimalist European heritage** with refined, modern-classic typography and restrained line-art illustration. The design is elegant, calm, and editorial -- never decorative or playful.

### Keywords

- Minimalist heritage
- European editorial wedding
- Fine-line architectural illustration
- Muted green and warm ivory palette
- Classic serif typography with elegant script accents
- Symmetrical, airy layout
- Understated luxury
- Timeless, not trendy
- Print-editorial inspired design

---

## Principles

### 1. Restraint Over Expression

Every element must earn its place. If removing something does not diminish the design, remove it. Decorative elements are few, purposeful, and cohesive with the illustration style.

### 2. Typographic Hierarchy First

The design is driven by typography, not imagery. Clear hierarchy through size, weight, case, and spacing -- not through color variation or decoration.

### 3. Generous White Space

White space is a design element, not empty space. Sections breathe. Content is never crowded. Margins and padding are generous. The layout feels editorial and print-like, not dense.

### 4. Visual Cohesion

All elements -- text, illustration, dividers, accents -- use the same primary green. There is no color variation beyond the defined palette. The site should feel like a single, unified artifact.

### 5. Symmetry and Balance

Center-aligned text. Symmetrical compositions. Balanced vertical rhythm. The layout is calm and ordered, never asymmetric or dynamic.

### 6. Mobile Dignity

The mobile experience is not a compressed desktop. It is designed with the same care for spacing, typography, and hierarchy. Guests will primarily view the site on their phones.

---

## Color Rules

See [DESIGN_TOKENS.md](./DESIGN_TOKENS.md) for exact values.

- **Restricted palette**: Only the five defined colors may be used. No additional colors.
- **No gradients**: Flat color only, everywhere.
- **No metallics or high-saturation tones**: The palette is muted and natural.
- **Low contrast**: Soft and sophisticated, not bold or punchy.
- **Consistent ink color**: Typography and illustration always use the same primary green.
- **Alternating section backgrounds**: `bg` and `bg-alt` alternate to create subtle visual breaks without introducing new colors.

---

## Typography Rules

See [DESIGN_TOKENS.md](./DESIGN_TOKENS.md) for exact values.

### PT Serif (headings, body, date, navigation)

- **Headings**: All-caps, wide letter-spacing (0.15em-0.25em). Classic Roman proportions. Clean and restrained, not ornate. Editorial and European.
- **Body text**: Regular case, normal tracking. Comfortable reading size.
- **Date**: All-caps, wide spacing between numbers and separators. Formal, balanced.
- **Navigation**: All-caps, wide tracking, smaller size.

### Petit Formal Script (names only)

- Used exclusively for "Isabell & Falk" -- the visual focal point.
- Elegant calligraphic feel. High-contrast strokes. Flowing but not overly flourished.
- Romantic and formal without being baroque.
- Never used for any other text element.

### General Rules

- No bold weights for emphasis. Use size, case, and spacing instead.
- No italic for emphasis (Petit Formal Script is inherently calligraphic).
- No underlined text except for links on hover.
- No text shadows or text effects.
- Line heights are generous (1.6-1.8 for body, 1.2-1.4 for headings).

---

## Illustration Rules

### Main Illustration (Hero)

- Monoline architectural line drawing of a European historic building (castle/gatehouse motif)
- Thin, consistent stroke weight
- Hand-drawn appearance but highly controlled
- Symmetrical composition
- Minimal shading using short hatch-like marks
- Flat, single-color: primary green (`#4A6856`)
- No fills, gradients, or textures
- SVG format, inline

### Section Dividers

- Simplified versions of the architectural motif (arches, pillars, keystones)
- Same stroke weight and color as the main illustration
- Horizontally centered
- Small and subtle -- they punctuate, not dominate
- Consistent style across all dividers

### General Rules

- All illustration elements use the same primary green as typography
- No photographic textures or raster decorations
- No icons from icon libraries (if icons are ever needed, they must match the monoline architectural style)
- No emoji or unicode decorative characters

---

## Layout Rules

- **Max content width**: ~800px, centered
- **Full-width section backgrounds**: Sections span the full viewport width; content is constrained within
- **Vertical rhythm**: Consistent spacing between sections (generous -- editorial, not compact)
- **Center alignment**: All text and elements are center-aligned
- **Section pattern**: Alternating `bg` / `bg-alt` backgrounds
- **No cards with borders or shadows**: If grouping content (e.g., accommodation), use spacing and subtle background shifts, not outlined cards
- **No horizontal scrolling**: Content adapts to viewport width
- **Smooth scroll**: CSS `scroll-behavior: smooth` for anchor navigation

---

## Interaction Rules

- **No animations or transitions** except: subtle hover color change on nav links and interactive elements
- **Hover state**: Links and nav items shift to `accent` green on hover
- **No parallax, no scroll effects, no fade-ins**
- **No JavaScript-driven interactions** (the site is pure HTML+CSS)
- **Focus states**: Visible and accessible, using the `accent` color

---

## What This Site Is Not

- Not playful or whimsical
- Not rustic or bohemian
- Not maximalist or colorful
- Not trendy (no glassmorphism, no neon, no dark mode)
- Not a template -- it is a bespoke design derived from the couple's save-the-date card
- Not image-heavy (typography and space do the work)
