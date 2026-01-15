# Frontend Fundamentals Workbook (JS + DOM + CSS)

Unified path through JavaScript essentials, DOM manipulation, and CSS layouts with applied labs. Consolidates the JavaScript Functions, DOM Manipulation, CSS Layout, and JavaScript Workshops guides.

## Table of Contents
1. JavaScript Essentials
2. DOM Basics & Events
3. CSS Layout Systems
4. Applied Labs (JS + DOM + CSS)
5. Capstone Mini-Project

---

## 1) JavaScript Essentials
- **Functions:** declarations vs expressions; arrow functions; hoisting rules; default params; rest/spread; higher-order functions (`map`, `filter`, `reduce`).
- **Scope & closures:** block vs function scope; closure patterns for encapsulation and factories.
- **Control flow:** guard clauses; early returns; error handling with `try/catch`.
- **Modules:** ES modules (`import/export`), named vs default exports; organizing utilities.
- **Async:** Promises, async/await, error handling patterns; sequencing vs parallel (`Promise.all`).

## 2) DOM Basics & Events
- **Selecting & traversing:** `querySelector(All)`, dataset, attributes, classes.
- **Creating/updating:** `createElement`, `append`, `prepend`, `replaceChildren`; template cloning for lists.
- **Events:** bubbling/capture; `addEventListener`; delegation for dynamic lists; preventing default; throttling/debouncing.
- **State in the DOM:** syncing data to UI; derived state from inputs; form handling; accessibility basics (labels, roles, focus management).
- **Fetching data:** `fetch` basics; rendering loading/error states; retry/backoff for flaky endpoints.

## 3) CSS Layout Systems
- **Box model fundamentals:** margin/padding/border/content; `box-sizing: border-box`.
- **Flexbox:** axis, `justify-content`, `align-items`, wrapping, gaps; common patterns (nav bars, cards).
- **Grid:** implicit vs explicit grids; repeat/auto-fit/auto-fill; gap; template areas for complex layouts.
- **Positioning & stacking:** relative/absolute/fixed; z-index with stacking contexts.
- **Responsive patterns:** mobile-first breakpoints; fluid typography; clamp(); container queries where supported.

## 4) Applied Labs (JS + DOM + CSS)
- **Lab 1: Interactive list manager**
  - Add/remove items with validation; use event delegation; persist in memory; keyboard accessibility.
  - Practice flex for controls and grid for list layout.
- **Lab 2: Fetch + render**
  - Fetch JSON, render cards with loading/error states; debounce search input; empty-state messaging.
  - Emphasize separation of data fetching and rendering functions for testability.
- **Lab 3: Form wizard**
  - Multi-step form with progress indicator; validation per step; summary screen.
  - Use CSS Grid for layout; manage state object that mirrors form fields.

## 5) Capstone Mini-Project
- Build a small single-page experience (e.g., task tracker or recipe finder) combining:
  - Componentized render functions (header, list, detail panel).
  - Accessible interactions (focus order, ARIA labels, keyboard shortcuts where appropriate).
  - Responsive layout (grid on desktop, stacked on mobile).
  - Basic persistence (localStorage) and error handling for network calls.
- Suggested milestones:
  1. Data model + mock data
  2. Layout scaffold (CSS Grid/Flex)
  3. Render pipeline + events
  4. Fetch integration + loading/error UI
  5. Polish: empty states, accessibility checks, small animations (transitions on hover/focus)

---

## See Also

- [JavaScript Functions Guide](JavaScript_Functions_Guide.md) - Deep dive into functions, closures, and higher-order functions
- [JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md) - Core JavaScript syntax and data types
- [DOM Manipulation Guide](DOM_Manipulation_Guide.md) - Comprehensive DOM manipulation patterns
- [JavaScript Async Programming Guide](JavaScript_Async_Programming_Guide.md) - Promises, async/await, and error handling
- [JavaScript Fetch API Guide](JavaScript_Fetch_API_Guide.md) - Fetching and rendering data from APIs
- [JavaScript LocalStorage Guide](JavaScript_LocalStorage_Guide.md) - Persisting data across sessions
- [CSS Layout Guide](CSS_Layout_Guide.md) - Flexbox and Grid fundamentals
- [CSS Flexbox Complete Guide](CSS_Flexbox_Complete_Guide.md) - Complete flexbox patterns and examples
- [CSS Grid Advanced Guide](CSS_Grid_Advanced_Guide.md) - Advanced grid layouts with template areas
- [HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md) - HTML structure and semantic markup
- [CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md) - CSS properties and selectors
