# CSS Layout Guide: Flexbox & Grid

Modern CSS layouts rely heavily on **Flexbox** (one-dimensional) and **Grid** (two-dimensional).

---

## 1. Flexbox (One-Dimensional)

Flexbox is best for arranging items in a single row or column. It excels at distributing space and aligning items.

### Container Properties (`display: flex`)

| Property | Values | Description |
| :--- | :--- | :--- |
| `flex-direction` | `row` (default), `column`, `row-reverse`, `column-reverse` | The direction items are placed. |
| `justify-content` | `flex-start`, `center`, `space-between`, `space-around`, `space-evenly` | Align items along the **main axis** (horizontal if row). |
| `align-items` | `stretch`, `center`, `flex-start`, `flex-end`, `baseline` | Align items along the **cross axis** (vertical if row). |
| `flex-wrap` | `nowrap`, `wrap` | Whether items should force onto one line or wrap. |

### Item Properties

| Property | Values | Description |
| :--- | :--- | :--- |
| `flex-grow` | Number (e.g., `1`) | How much the item will grow relative to others. |
| `flex-shrink` | Number (e.g., `1`) | How much the item will shrink if space is tight. |
| `flex-basis` | Length (e.g., `20%`, `auto`) | The initial size of the item. |

**Example:**
```css
.container {
    display: flex;
    justify-content: space-between; /* Space items out */
    align-items: center; /* Center vertically */
}

.item {
    flex: 1; /* Grow to fill space */
}
```

---

## 2. CSS Grid (Two-Dimensional)

Grid is best for page layouts where you need to control both rows and columns simultaneously.

### Container Properties (`display: grid`)

| Property | Example | Description |
| :--- | :--- | :--- |
| `grid-template-columns` | `1fr 1fr 1fr`, `200px auto` | Defines the size of columns. `fr` is a fraction unit. |
| `grid-template-rows` | `100px auto 50px` | Defines the size of rows. |
| `gap` | `10px`, `1rem` | Space between grid cells (both row and column). |
| `grid-template-areas` | `"header header" "sidebar main"` | Defines named areas for layout. |

### Item Properties

| Property | Example | Description |
| :--- | :--- | :--- |
| `grid-column` | `1 / 3` | Span from column line 1 to 3. |
| `grid-row` | `2 / 4` | Span from row line 2 to 4. |
| `grid-area` | `header` | Assign item to a named area. |

**Example:**
```css
.grid-container {
    display: grid;
    grid-template-columns: 200px 1fr; /* Sidebar fixed, content flexes */
    gap: 20px;
}

.sidebar {
    grid-column: 1 / 2;
}

.main-content {
    grid-column: 2 / 3;
}
```

---

## 3. Positioning (The Old Way & Overlays)

While Flexbox and Grid handle structure, `position` is still critical for overlays, sticky headers, and specific tweaks.

*   **Relative**: The element remains in the flow but can be nudged using `top`, `left`.
*   **Absolute**: Removed from flow. Positioned relative to the nearest *positioned* ancestor (usually a parent with `position: relative`).
*   **Fixed**: Pinned to the viewport (e.g., a "Back to Top" button).
*   **Sticky**: Acts like relative until you scroll past it, then becomes fixed (e.g., a sticky nav bar).

**Common Pattern (Overlay Text on Image):**
```css
.card {
    position: relative; /* Parent */
}

.card-text {
    position: absolute; /* Child */
    bottom: 10px;
    left: 10px;
    color: white;
}
```

---

## See Also

- **[CSS Cheat Sheet](./CSS_Cheat_Sheet.md)** - Basic CSS properties
- **[HTML Cheat Sheet](./HTML_Cheat_Sheet.md)** - HTML structure