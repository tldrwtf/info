# HTML5 Cheat Sheet

**HTML (HyperText Markup Language)** is the standard markup language for creating web pages. It describes the structure of a Web page.

## Basic Structure

Every HTML document should follow this boilerplate structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

## Common Tags

### Text Formatting
*   `<h1>` to `<h6>`: Headings (h1 is the most important).
*   `<p>`: Paragraph.
*   `<strong>` or `<b>`: **Bold** text.
*   `<em>` or `<i>`: *Italic* text.
*   `<span>`: Inline container for text (no semantic meaning).
*   `<br>`: Line break (self-closing).
*   `<hr>`: Horizontal rule (thematic break).

### Containers (Semantic)
*   `<div>`: Block-level container (generic).
*   `<header>`: Introductory content or navigational links.
*   `<nav>`: Navigation links.
*   `<main>`: The dominant content of the `<body>`.
*   `<section>`: A thematic grouping of content.
*   `<article>`: Independent, self-contained content (e.g., blog post).
*   `<aside>`: Content aside from the page content (e.g., sidebar).
*   `<footer>`: Footer for a section or page.

### Lists
**Unordered List (Bullet points)**
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
```

**Ordered List (Numbered)**
```html
<ol>
    <li>First Item</li>
    <li>Second Item</li>
</ol>
```

### Links & Images
**Anchor Tag (Links)**
```html
<a href="https://google.com" target="_blank">Go to Google</a>
<!-- target="_blank" opens in a new tab -->
```

**Image Tag**
```html
<img src="image.jpg" alt="Description of image" width="300">
<!-- 'alt' is crucial for accessibility -->
```

## Tables

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>25</td>
        </tr>
    </tbody>
</table>
```

## Forms

```html
<form action="/submit" method="POST">
    <!-- Text Input -->
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>

    <!-- Password -->
    <label for="pwd">Password:</label>
    <input type="password" id="pwd" name="password">

    <!-- Radio Buttons -->
    <input type="radio" name="gender" value="male"> Male
    <input type="radio" name="gender" value="female"> Female

    <!-- Checkbox -->
    <input type="checkbox" name="newsletter" checked> Subscribe?

    <!-- Dropdown -->
    <select name="cars">
        <option value="volvo">Toyota</option>
        <option value="saab">Honda</option>
    </select>

    <button type="submit">Submit</button>
</form>
```

## Attributes
*   `id`: Unique identifier for an element.
*   `class`: Class name(s) for CSS styling (can be reused).
*   `style`: Inline CSS styles.
*   `title`: Tooltip text when hovering.
*   `data-*`: Custom data attributes (e.g., `data-user-id="123"`).

---

## See Also

- **[CSS Cheat Sheet](./CSS_Cheat_Sheet.md)** - Styling your HTML
- **[CSS Layout Guide](./CSS_Layout_Guide.md)** - Structuring pages with Flexbox and Grid
- **[JavaScript Basics Cheat Sheet](./JavaScript_Basics_Cheat_Sheet.md)** - Scripting