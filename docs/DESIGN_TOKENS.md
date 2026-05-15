# Design Tokens

Concrete values for implementing the design constitution. These are the single source of truth for all color, typography, and spacing decisions in the codebase.

---

## Colors

| Token     | Hex       | RGB             | Usage                                                                                                           |
| --------- | --------- | --------------- | --------------------------------------------------------------------------------------------------------------- |
| `primary` | `#4A6856` | `74, 104, 86`   | All text, headings, nav, dividers, illustration, accents (darkened from #4F6F5B for WCAG AA contrast on bg-alt) |
| `bg`      | `#F4F1E8` | `244, 241, 232` | Main page background (warm ivory)                                                                               |
| `bg-alt`  | `#E9E4D6` | `233, 228, 214` | Alternating section backgrounds                                                                                 |
| `accent`  | `#456650` | `69, 102, 80`   | Hover states, links on hover, subtle UI highlights                                                              |
| `body`    | `#2F3A33` | `47, 58, 51`    | Long-form body text (improved readability, use sparingly)                                                       |

### Tailwind Config

```js
colors: {
  primary: '#4A6856',
  bg: '#F4F1E8',
  'bg-alt': '#E9E4D6',
  accent: '#456650',
  body: '#2F3A33',
}
```

### Usage Rules

- `primary` is the dominant color. Used for all headings, navigation, decorative elements, dividers, and illustration strokes.
- `bg` is the default page background. Alternates with `bg-alt` per section.
- `bg-alt` is only for alternating section backgrounds and subtle panels. Never used for text or accents.
- `accent` is reserved for interactive states (hover, focus). Not used in static design.
- `body` is optional for long-form text blocks where `primary` may feel too light for extended reading. Use sparingly -- most text should use `primary`.

---

## Typography

### Font Families

| Token    | Font                | Google Fonts URL                                                                             |
| -------- | ------------------- | -------------------------------------------------------------------------------------------- |
| `script` | Petit Formal Script | `https://fonts.googleapis.com/css2?family=Petit+Formal+Script&display=swap`                  |
| `serif`  | PT Serif            | `https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400&display=swap` |

### Tailwind Config

```js
fontFamily: {
  serif: ['"PT Serif"', 'Georgia', 'serif'],
  script: ['"Petit Formal Script"', 'cursive'],
}
```

### Type Scale

| Element          | Font                | Size (desktop)   | Size (mobile)    | Weight | Case       | Letter Spacing | Line Height |
| ---------------- | ------------------- | ---------------- | ---------------- | ------ | ---------- | -------------- | ----------- |
| Names (hero)     | Petit Formal Script | 3rem (48px)      | 2rem (32px)      | 400    | As written | normal         | 1.2         |
| Section headings | PT Serif            | 1.25rem (20px)   | 1.125rem (18px)  | 400    | uppercase  | 0.2em          | 1.3         |
| Subheadings      | PT Serif            | 1.125rem (18px)  | 1rem (16px)      | 400    | uppercase  | 0.15em         | 1.3         |
| Body text        | PT Serif            | 1.0625rem (17px) | 1rem (16px)      | 400    | normal     | normal         | 1.7         |
| Navigation links | PT Serif            | 0.8125rem (13px) | 0.75rem (12px)   | 400    | uppercase  | 0.2em          | 1.0         |
| Date (hero)      | PT Serif            | 1.125rem (18px)  | 1rem (16px)      | 400    | uppercase  | 0.25em         | 1.3         |
| Footer text      | PT Serif            | 0.875rem (14px)  | 0.8125rem (13px) | 400    | normal     | 0.1em          | 1.5         |

---

## Spacing

### Section Padding

| Breakpoint | Vertical padding (per section) |
| ---------- | ------------------------------ |
| Mobile     | `4rem` (64px) top and bottom   |
| Desktop    | `6rem` (96px) top and bottom   |

### Content Width

| Token           | Value           |
| --------------- | --------------- |
| `max-w-content` | `52rem` (832px) |

### Element Spacing

| Between                     | Spacing          |
| --------------------------- | ---------------- |
| Section heading and content | `2rem` (32px)    |
| Body paragraphs             | `1.25rem` (20px) |
| Timeline entries            | `1.5rem` (24px)  |
| Accommodation cards         | `2rem` (32px)    |
| Divider and section edge    | `3rem` (48px)    |

---

## Illustration

### Stroke Properties

| Property        | Value           |
| --------------- | --------------- |
| Stroke color    | `#4A6856`       |
| Stroke width    | `1px` - `1.5px` |
| Stroke linecap  | `round`         |
| Stroke linejoin | `round`         |
| Fill            | `none`          |

### Sizing

| Element           | Width (desktop)   | Width (mobile)    |
| ----------------- | ----------------- | ----------------- |
| Hero illustration | `300px` - `400px` | `200px` - `280px` |
| Section dividers  | `80px` - `120px`  | `60px` - `100px`  |

---

## Responsive Breakpoints

| Name    | Min width | Notes                  |
| ------- | --------- | ---------------------- |
| Mobile  | 0         | Default / mobile-first |
| Tablet  | `640px`   | `sm:` in Tailwind      |
| Desktop | `1024px`  | `lg:` in Tailwind      |

---

## Divider Style

Simple horizontal rule between subsections (not between major sections, which use SVG architectural dividers):

```css
/* Thin line in primary color */
border: none;
border-top: 1px solid #4a6856;
opacity: 0.3;
width: 4rem;
margin: 2rem auto;
```
