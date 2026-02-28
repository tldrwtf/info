# Bootstrap Components and Custom Grid Guide

Use Bootstrap for fast, accessible UI primitives while using CSS Grid for full-page layout control.

## Quick Reference Card

| Concept | Example | Why It Matters |
|---------|---------|----------------|
| **Bootstrap CSS** | `<link ... bootstrap.min.css>` | Base styling, utilities, and components |
| **Bootstrap JS Bundle** | `<script ... bootstrap.bundle.min.js defer>` | Enables collapses, modals, carousels, dropdowns |
| **Responsive Navbar** | `.navbar .navbar-expand-lg` | Mobile-first navigation with collapse behavior |
| **Cards + Utilities** | `.card`, `.shadow-sm`, `.mb-3` | Fast content blocks with consistent spacing |
| **Form Controls** | `.form-control`, `.form-check` | Accessible default styling and form ergonomics |
| **Custom Page Grid** | `grid-template-areas` | Clear macro-layout beyond Bootstrap row/col |
| **Hybrid Strategy** | Bootstrap inside grid areas | Best of both systems without fighting either |

---

## Table of Contents
1. [When to Use Bootstrap vs Custom Grid](#1-when-to-use-bootstrap-vs-custom-grid)
2. [Setup and Project Baseline](#2-setup-and-project-baseline)
3. [Core Bootstrap Components in Practice](#3-core-bootstrap-components-in-practice)
4. [Hybrid Layout Architecture (Bootstrap + CSS Grid)](#4-hybrid-layout-architecture-bootstrap--css-grid)
5. [Responsive Reconfiguration](#5-responsive-reconfiguration)
6. [Accessibility and Performance](#6-accessibility-and-performance)
7. [Common Pitfalls](#7-common-pitfalls)
8. [Mini Project Blueprint](#8-mini-project-blueprint)
9. [Production Checklist](#9-production-checklist)

---

## 1. When to Use Bootstrap vs Custom Grid

Use **Bootstrap** for:
- Reusable UI components (navbar, cards, forms, modals, alerts).
- Utility classes (`d-flex`, `gap-3`, `mt-4`, `text-center`) to reduce custom CSS.
- Consistent defaults and responsive behavior quickly.

Use **CSS Grid** for:
- Page shell layout (header, nav, content, aside, footer).
- Complex spatial relationships (`grid-template-areas`).
- Large breakpoint-driven layout rewrites.

Practical rule:
- **Macro layout**: custom Grid.
- **Micro layout and components**: Bootstrap.

---

## 2. Setup and Project Baseline

### CDN setup

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bootstrap + Grid Hybrid</title>

  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
    rel="stylesheet"
  />

  <link rel="stylesheet" href="./styles.css" />

  <script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
    defer
  ></script>
</head>
<body>
  <!-- Content -->
</body>
</html>
```

### Baseline CSS reset

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
}
```

---

## 3. Core Bootstrap Components in Practice

### Responsive navbar

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary border-bottom">
  <div class="container-fluid">
    <a class="navbar-brand fw-bold" href="#">InfoHub</a>

    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#mainNav"
      aria-controls="mainNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="mainNav">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Guides</a></li>
        <li class="nav-item"><a class="nav-link" href="#">About</a></li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search guides" />
        <button class="btn btn-outline-primary" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

### Carousel with predictable image behavior

```html
<div id="heroCarousel" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./assets/slide-1.jpg" class="d-block w-100 carousel-img" alt="Laptop and notebook on desk" />
    </div>
    <div class="carousel-item">
      <img src="./assets/slide-2.jpg" class="d-block w-100 carousel-img" alt="Team planning in office" />
    </div>
  </div>

  <button class="carousel-control-prev" type="button" data-bs-target="#heroCarousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#heroCarousel" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```

```css
.carousel-img {
  height: clamp(220px, 45vh, 480px);
  object-fit: cover;
}
```

### Cards + form section

```html
<section class="container py-4">
  <div class="row g-3">
    <div class="col-12 col-md-6 col-xl-4">
      <article class="card h-100 shadow-sm">
        <div class="card-body">
          <h2 class="h5 card-title">Async JavaScript</h2>
          <p class="card-text">Promises, await, cancellation, and retries.</p>
          <a href="#" class="btn btn-primary">Read guide</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="container pb-5">
  <form class="p-4 border rounded-3 bg-light-subtle">
    <h2 class="h5 mb-3">Join Newsletter</h2>

    <div class="mb-3">
      <label for="email" class="form-label">Email address</label>
      <input id="email" type="email" class="form-control" required />
    </div>

    <div class="form-check mb-3">
      <input id="terms" type="checkbox" class="form-check-input" required />
      <label for="terms" class="form-check-label">I agree to receive updates</label>
    </div>

    <button class="btn btn-success" type="submit">Subscribe</button>
  </form>
</section>
```

---

## 4. Hybrid Layout Architecture (Bootstrap + CSS Grid)

### HTML shell

```html
<body class="layout">
  <header class="area-header">
    <!-- carousel -->
  </header>

  <nav class="area-nav">
    <!-- navbar -->
  </nav>

  <main class="area-main">
    <!-- Bootstrap cards/content -->
  </main>

  <aside class="area-aside p-3 border-start bg-body-tertiary">
    <!-- quick links, filters, ads -->
  </aside>

  <footer class="area-footer py-3 text-center border-top">
    Copyright 2026
  </footer>
</body>
```

### Grid map

```css
.layout {
  display: grid;
  min-height: 100vh;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: auto auto 1fr auto;
  grid-template-areas:
    "header header"
    "nav nav"
    "main aside"
    "footer footer";
}

.area-header { grid-area: header; }
.area-nav { grid-area: nav; }
.area-main { grid-area: main; }
.area-aside { grid-area: aside; }
.area-footer { grid-area: footer; }
```

Why this works:
- Grid controls page-level placement.
- Bootstrap controls spacing, typography, and component internals.
- You avoid overusing nested `.row/.col` for full-page composition.

---

## 5. Responsive Reconfiguration

Use media queries to rewrite the page map, not all individual components.

```css
@media (max-width: 991.98px) {
  .layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "nav"
      "main"
      "aside"
      "footer";
  }

  .area-aside {
    border-left: 0;
    border-top: 1px solid var(--bs-border-color);
  }
}
```

Use Bootstrap breakpoints for components and custom breakpoints for grid shell changes.

---

## 6. Accessibility and Performance

### Accessibility

- Keep semantic regions: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`.
- Add meaningful alt text for carousel images.
- Ensure navbar toggler has `aria-*` attributes.
- Maintain visible focus styles; do not globally remove outlines.
- Preserve color contrast when overriding Bootstrap variables.

### Performance

- Load only one Bootstrap CSS/JS source (avoid duplicate includes).
- Prefer `bootstrap.bundle.min.js` so Popper is included once.
- Compress and size carousel images; `object-fit` does not reduce file weight.
- Avoid deep selector overrides; use utility classes and CSS variables when possible.

---

## 7. Common Pitfalls

1. **Including custom CSS before Bootstrap**
   Your overrides get overwritten.
2. **Mixing grid systems in the same layer**
   Use Bootstrap grid *inside* components and CSS Grid for page shell.
3. **Missing viewport meta tag**
   Mobile layout and breakpoints behave incorrectly.
4. **Forgetting JS bundle**
   Components like collapse and carousel stop functioning.
5. **Hard-coded carousel heights in pixels only**
   Causes poor mobile experience; use `clamp()`.
6. **Inline `style` for layout rules**
   Harder to maintain; move layout logic into CSS classes.

---

## 8. Mini Project Blueprint

Build a "Guide Portal" page:
1. Hero carousel in `header`.
2. Sticky navbar below header.
3. `main` area with Bootstrap cards for guide categories.
4. `aside` with filters and "popular guides" list.
5. Newsletter form in footer or aside.

Stretch goals:
- Add dark/light theme with Bootstrap data attributes.
- Add modal for "quick preview" of a guide card.
- Add form validation feedback (`is-invalid`, `invalid-feedback`).

---

## 9. Production Checklist

- [ ] Bootstrap CSS loaded before custom stylesheet.
- [ ] Bootstrap bundle loaded with `defer`.
- [ ] Semantic layout regions mapped with `grid-template-areas`.
- [ ] Grid reconfiguration tested at mobile/tablet/desktop widths.
- [ ] Interactive components keyboard accessible.
- [ ] Images optimized and responsive.
- [ ] No layout-critical inline styles.

---

## See Also
- [Bootstrap Cheat Sheet](../cheatsheets/Bootstrap_Cheat_Sheet.md)
- [CSS Grid Advanced Guide](./CSS_Grid_Advanced_Guide.md)
- [CSS Layout Guide](./CSS_Layout_Guide.md)
- [CSS Flexbox Complete Guide](./CSS_Flexbox_Complete_Guide.md)
- [Frontend Fundamentals Workbook](./Frontend_Fundamentals_Workbook.md)
