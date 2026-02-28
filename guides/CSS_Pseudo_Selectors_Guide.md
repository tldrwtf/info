# CSS Pseudo-Classes and Pseudo-Elements Guide

Master state-driven styling and virtual element techniques without extra markup.

## Quick Reference Card

| Concept | Syntax | Why It Matters |
|---------|--------|----------------|
| **Interactive State** | `:hover`, `:focus-visible` | Better UX for pointer and keyboard users |
| **Form State** | `:required`, `:invalid`, `:checked` | Native validation and input feedback |
| **Structural Selection** | `:nth-child(2n)`, `:first-child` | Pattern-based styling without extra classes |
| **Negation / Grouping** | `:not(...)`, `:is(...)`, `:where(...)` | Cleaner selectors with controlled specificity |
| **Parent-aware Selection** | `:has(...)` | Style container based on child state/content |
| **Virtual Elements** | `::before`, `::after` | Decorative or semantic UI enhancements |
| **Text Fragments** | `::first-letter`, `::selection` | Typography and text interaction polish |

---

## Table of Contents
1. [Pseudo-Class vs Pseudo-Element](#1-pseudo-class-vs-pseudo-element)
2. [Interactive and Accessibility States](#2-interactive-and-accessibility-states)
3. [Structural Pseudo-Classes](#3-structural-pseudo-classes)
4. [Form and Validation States](#4-form-and-validation-states)
5. [Specificity-Smart Selectors (`:is`, `:where`, `:not`, `:has`)](#5-specificity-smart-selectors-is-where-not-has)
6. [Pseudo-Elements in Real UI](#6-pseudo-elements-in-real-ui)
7. [Practical Patterns](#7-practical-patterns)
8. [Common Pitfalls](#8-common-pitfalls)
9. [Practice Drills](#9-practice-drills)
10. [Production Checklist](#10-production-checklist)

---

## 1. Pseudo-Class vs Pseudo-Element

- **Pseudo-class (`:`)** targets an element in a state or condition.
  - Example: `button:hover`, `input:invalid`, `li:nth-child(odd)`.
- **Pseudo-element (`::`)** targets part of an element or inserts virtual content.
  - Example: `p::first-line`, `.link::after`.

Quick memory aid:
- Pseudo-class = "this element when..."
- Pseudo-element = "this part of this element"

---

## 2. Interactive and Accessibility States

### Prefer `:focus-visible` over `:focus` for keyboard ergonomics

```css
a {
  text-decoration: none;
  color: #1f3c88;
}

a:hover {
  color: #10306f;
}

a:focus-visible {
  outline: 3px solid #0ea5e9;
  outline-offset: 2px;
  border-radius: 4px;
}
```

Use cases:
- `:hover` for pointer interactions.
- `:focus-visible` for accessible keyboard focus rings.
- `:active` for press feedback.

### Group interaction states safely

```css
.button:is(:hover, :focus-visible) {
  transform: translateY(-1px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
}
```

---

## 3. Structural Pseudo-Classes

### `:nth-child()` patterns

```css
.list-item:nth-child(odd) {
  background: #f8fafc;
}

.list-item:nth-child(even) {
  background: #eef2ff;
}

.list-item:nth-child(3n) {
  border-left: 4px solid #6366f1;
}
```

### Common structure selectors

```css
.card:first-child {
  margin-top: 0;
}

.card:last-child {
  margin-bottom: 0;
}

.menu-item:not(:last-child) {
  border-bottom: 1px solid #e2e8f0;
}
```

### `:nth-of-type()` vs `:nth-child()`

- `:nth-child()` counts all siblings.
- `:nth-of-type()` counts siblings of the same element type only.

Use `:nth-of-type()` when mixed tags are present.

---

## 4. Form and Validation States

Browser-native state selectors help build robust forms quickly.

```css
input:required {
  border-left: 4px solid #f59e0b;
}

input:invalid {
  border-color: #dc2626;
}

input:valid {
  border-color: #16a34a;
}

input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

input:checked + label {
  font-weight: 700;
  color: #1d4ed8;
}
```

Tip: show errors only after user interaction to avoid "red form on first paint".

```css
input:user-invalid {
  border-color: #dc2626;
}
```

(Use where supported and combine with JS for full compatibility.)

---

## 5. Specificity-Smart Selectors (`:is`, `:where`, `:not`, `:has`)

### `:is()` to reduce repetition

```css
:is(h1, h2, h3) {
  line-height: 1.2;
  letter-spacing: -0.02em;
}
```

### `:where()` for zero-specificity wrappers

```css
:where(.prose) p {
  margin-block: 1rem;
}
```

` :where()` contributes zero specificity, great for design-system base styles.

### `:not()` for exclusion

```css
.button:not(.button--secondary) {
  background: #2563eb;
  color: #fff;
}
```

### `:has()` for parent-aware styling

```css
.card:has(img) {
  padding-top: 0;
}

.form-group:has(input:focus-visible) {
  box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.25);
  border-radius: 8px;
}
```

Use `:has()` when parent style must react to child state. If supporting older browsers, provide fallback class toggles via JavaScript.

---

## 6. Pseudo-Elements in Real UI

### `::before` and `::after`

`content` is required, even when empty.

```css
.link {
  position: relative;
  color: #1e293b;
}

.link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 200ms ease;
}

.link:is(:hover, :focus-visible)::after {
  transform: scaleX(1);
}
```

### Typography fragments

```css
.article-intro::first-letter {
  float: left;
  font-size: 2.5rem;
  line-height: 0.9;
  margin-right: 0.4rem;
  font-weight: 700;
}

.article-intro::first-line {
  color: #334155;
}
```

### Selection and placeholders

```css
::selection {
  background: #fde68a;
  color: #111827;
}

input::placeholder {
  color: #94a3b8;
  font-style: italic;
}
```

---

## 7. Practical Patterns

### Pattern 1: Zebra table rows without extra classes

```css
tbody tr:nth-child(even) {
  background: #f8fafc;
}
```

### Pattern 2: Add separators except last item

```css
.breadcrumb-item:not(:last-child)::after {
  content: ">";
  margin-inline: 0.5rem;
  color: #94a3b8;
}
```

### Pattern 3: Highlight current nav item by URL state class

```css
.nav-link[aria-current="page"] {
  color: #0f172a;
  font-weight: 700;
}
```

### Pattern 4: Card accent when child button focused

```css
.card:has(.card-cta:focus-visible) {
  outline: 2px solid #38bdf8;
  outline-offset: 2px;
}
```

---

## 8. Common Pitfalls

1. **Using `:focus` and removing outline globally**
   Harms keyboard accessibility.
2. **Confusing single and double colon forms**
   Modern pseudo-elements use `::`.
3. **Forgetting `content` for `::before/::after`**
   Nothing renders.
4. **Overly complex selectors**
   Harder to maintain and debug than utility classes or component classes.
5. **Unplanned specificity escalation**
   Avoid selector wars; use `:where()` for base styles and scoped class names.
6. **Assuming full `:has()` support in all target environments**
   Add graceful fallback strategy when needed.

---

## 9. Practice Drills

1. Build a nav link underline animation using `::after`.
2. Style invalid/valid form fields using only CSS state selectors.
3. Create zebra rows and every-third-row accents in a data table.
4. Use `:has()` to highlight a card when any child input is focused.
5. Refactor repeated selectors into one `:is(...)` rule.

---

## 10. Production Checklist

- [ ] Interactive elements have visible `:focus-visible` styles.
- [ ] `::before/::after` rules include `content`.
- [ ] Structural selectors are readable and intentional.
- [ ] Specificity remains predictable (`:where` for low-specificity base rules).
- [ ] Form states (`:invalid`, `:disabled`, `:checked`) are covered.
- [ ] Browser support for advanced selectors (especially `:has`) is verified.

---

## See Also
- [CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md)
- [CSS Layout Guide](./CSS_Layout_Guide.md)
- [CSS Grid Advanced Guide](./CSS_Grid_Advanced_Guide.md)
- [CSS Flexbox Complete Guide](./CSS_Flexbox_Complete_Guide.md)
- [DOM Manipulation Guide](./DOM_Manipulation_Guide.md)
