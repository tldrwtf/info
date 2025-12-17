# Bootstrap 5 Cheat Sheet

Bootstrap is the most popular CSS framework for developing responsive and mobile-first websites. It provides pre-built components and a powerful grid system.

## Quick Reference Card

| Concept | Class Syntax | Example |
| :--- | :--- | :--- |
| **Container** | `.container` / `.container-fluid` | `<div class="container">` |
| **Grid Row** | `.row` | `<div class="row">` |
| **Grid Column** | `.col-{breakpoint}-{width}` | `<div class="col-md-6">` |
| **Margin/Padding** | `{property}{side}-{size}` | `m-3` (Margin 3), `pt-2` (Padding Top 2) |
| **Flexbox** | `.d-flex` | `<div class="d-flex justify-content-center">` |
| **Colors** | `.text-{color}` / `.bg-{color}` | `.text-primary`, `.bg-light` |
| **Display** | `.d-{breakpoint}-{value}` | `.d-none`, `.d-md-block` |

## Table of Contents
- [Setup & CDN](#setup--cdn)
- [Layout & Grid](#layout--grid)
- [Typography & Colors](#typography--colors)
- [Spacing Utilities](#spacing-utilities)
- [Components](#components)
    - [Navbar](#navbar)
    - [Buttons](#buttons)
    - [Cards](#cards)
    - [Forms](#forms)
    - [Carousel](#carousel)

---

## Setup & CDN

Include these in your `index.html` `head` (CSS) and `body` (JS bundle).

### CSS (Head)
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-..." crossorigin="anonymous">
```

### JS Bundle (End of Body)
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-..." crossorigin="anonymous"></script>
```

---

## Layout & Grid

Bootstrap's grid system uses a series of containers, rows, and columns to layout and align content. It's built with flexbox and is fully responsive.

### Containers
*   `.container`: Fixed width container, responsive at breakpoints.
*   `.container-fluid`: Full width container, spans the entire width of the viewport.

### The 12-Column Grid
Rows are wrappers for columns. Each row has 12 "slots". Columns must add up to 12 (or fewer).

```html
<div class="container">
  <div class="row">
    <!-- Two equal columns (6 + 6 = 12) -->
    <div class="col-6">Left Half</div>
    <div class="col-6">Right Half</div>
  </div>
  
  <div class="row">
    <!-- Three columns (4 + 4 + 4 = 12) -->
    <div class="col-4">One Third</div>
    <div class="col-4">One Third</div>
    <div class="col-4">One Third</div>
  </div>
</div>
```

### Responsive Breakpoints
Add specific prefixes to target screen sizes.

| Breakpoint | Class Prefix | Dimension |
| :--- | :--- | :--- |
| **X-Small** | `.col-` | <576px |
| **Small** | `.col-sm-` | ≥576px |
| **Medium** | `.col-md-` | ≥768px |
| **Large** | `.col-lg-` | ≥992px |
| **X-Large** | `.col-xl-` | ≥1200px |

**Example:**
```html
<!-- Stack on mobile, side-by-side on desktop -->
<div class="row">
  <div class="col-12 col-md-6">Content A</div>
  <div class="col-12 col-md-6">Content B</div>
</div>
```

---

## Typography & Colors

### Text Alignment
*   `.text-start` (Left)
*   `.text-center` (Center)
*   `.text-end` (Right)

### Theme Colors
Apply to text (`.text-`) or backgrounds (`.bg-`).

*   `primary` (Blue)
*   `secondary` (Grey)
*   `success` (Green)
*   `danger` (Red)
*   `warning` (Yellow)
*   `info` (Cyan)
*   `light` (White/Light Grey)
*   `dark` (Black/Dark Grey)

```html
<p class="text-danger bg-dark">Red text on dark background</p>
```

---

## Spacing Utilities

Format: `{property}{sides}-{size}`

*   **Property:** `m` (margin), `p` (padding)
*   **Sides:**
    *   `t` (top), `b` (bottom), `s` (start/left), `e` (end/right)
    *   `x` (left & right), `y` (top & bottom)
    *   *(blank)* (all 4 sides)
*   **Size:** `0` (none) to `5` (largest), `auto`

**Examples:**
*   `m-0`: Remove margin.
*   `p-3`: Medium padding all around.
*   `my-5`: Large vertical margin.
*   `me-auto`: Margin-right auto (pushes items to the left in flexbox).

---

## Components

### Navbar
Standard navigation header.

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">MyApp</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

### Buttons
```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-outline-secondary">Secondary Outline</button>
<button type="button" class="btn btn-lg btn-danger">Large Danger</button>
```

### Cards
Container for content.

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

### Forms
Bootstrap automatically styles inputs.

```html
<form>
  <div class="mb-3">
    <label for="emailInput" class="form-label">Email address</label>
    <input type="email" class="form-control" id="emailInput">
    <div id="emailHelp" class="form-text">We'll never share your email.</div>
  </div>
  <div class="mb-3">
    <label for="passInput" class="form-label">Password</label>
    <input type="password" class="form-control" id="passInput">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### Carousel
Image slider.

```html
<div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
  </button>
</div>
```

---

## See Also
- **[CSS Cheat Sheet](CSS_Cheat_Sheet.md)** - Pure CSS reference.
- **[CSS Layout Guide](../guides/CSS_Layout_Guide.md)** - Flexbox and Grid deep dive.
