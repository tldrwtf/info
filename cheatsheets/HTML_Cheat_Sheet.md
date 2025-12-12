# HTML5 Cheat Sheet

**HTML (HyperText Markup Language)** is the standard markup language for creating web pages. It describes the structure of a Web page.

---

## 1. Basic Structure (Boilerplate)

Every HTML document should follow this boilerplate structure, which includes essential metadata for responsiveness and character encoding.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <!-- Link to external CSS stylesheets -->
    <link rel="stylesheet" href="styles/main.css">
    <!-- Link to external JavaScript files -->
    <script src="scripts/main.js" defer></script>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

## 2. Document Head (`<head>`) Elements

These elements provide metadata about the document and link to external resources.

*   `<meta charset="UTF-8">`: Specifies the character encoding for the document.
*   `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Configures the viewport for responsive design.
*   `<title>Page Title</title>`: Sets the title that appears in the browser tab.
*   `<link rel="stylesheet" href="path/to/style.css">`: Links an external stylesheet.
*   `<script src="path/to/script.js" defer></script>`: Links an external JavaScript file. `defer` ensures the script runs after HTML parsing.

## 3. Common Tags & Semantic Elements

HTML5 introduced several semantic elements that clearly describe their meaning to both the browser and the developer, improving accessibility and SEO.

### Text Formatting
*   `<h1>` to `<h6>`: Headings, with `<h1>` being the most important.
*   `<p>`: Paragraph for blocks of text.
*   `<strong>` or `<b>`: **Bold** text (semantically `<strong>` indicates importance).
*   `<em>` or `<i>`: *Italic* text (semantically `<em>` indicates emphasis).
*   `<span>`: An inline container for text, primarily for styling purposes (no semantic meaning).
*   `<br>`: Line break (self-closing tag).
*   `<hr>`: Horizontal rule, a thematic break between paragraph-level elements.

### Semantic Sectioning Elements
These elements help define the structure and hierarchy of your web page.

*   `<header>`: Represents introductory content, typically containing a group of introductory or navigational aids.
*   `<nav>`: Contains navigation links, either to the current document or to other documents.
*   `<main>`: Represents the dominant content of the `<body>` of a document. There should only be one per document.
*   `<section>`: A standalone section that doesn't have a more specific semantic element to represent it. Often has a heading.
*   `<article>`: Represents self-contained content that could be distributed independently (e.g., a blog post, a newspaper article).
*   `<aside>`: Represents a portion of a document whose content is indirectly related to the document's main content; often presented as a sidebar.
*   `<footer>`: Represents a footer for its nearest sectioning content or sectioning root. Typically contains authorship information, copyright data, or links to related documents.
*   `<div>`: A generic block-level container. Use when no other semantic element is appropriate.

### Lists
**Unordered List (`<ul>` - Bullet points)**
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

**Ordered List (`<ol>` - Numbered list)**
```html
<ol>
    <li>First Item</li>
    <li>Second Item</li>
    <li>Third Item</li>
</ol>
```

**Description List (`<dl>` - Key-value pairs)**
```html
<dl>
    <dt>Coffee</dt>
    <dd>Black hot drink</dd>
    <dt>Milk</dt>
    <dd>White cold drink</dd>
</dl>
```

### Links & Images
**Anchor Tag (`<a>` - Hyperlinks)**
```html
<a href="https://www.google.com" target="_blank" title="Go to Google">Go to Google</a>
<!-- `target="_blank"` opens the link in a new tab -->
<!-- `title` provides a tooltip on hover -->
```

**Image Tag (`<img>`)**
```html
<img src="images/profile.jpg" alt="Description of image" width="300" height="200">
<!-- `alt` is crucial for accessibility and SEO -->
<!-- `width` and `height` provide intrinsic sizing, reducing layout shifts -->
```

## 4. Tables

Tables are used to display tabular data.

```html
<table>
    <caption>Monthly Sales Report</caption>
    <thead>
        <tr>
            <th>Month</th>
            <th>Sales</th>
            <th>Profit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>January</td>
            <td>$1000</td>
            <td>$300</td>
        </tr>
        <tr>
            <td>February</td>
            <td>$1200</td>
            <td>$350</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>Total</td>
            <td>$2200</td>
            <td>$650</td>
        </tr>
    </tfoot>
</table>
```

## 5. Forms (`<form>`)

Forms are used to collect user input.

```html
<form action="/submit-data" method="POST">
    <fieldset>
        <legend>Personal Information</legend>

        <!-- Text Input -->
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" name="first_name" required placeholder="Enter your first name">

        <!-- Email Input -->
        <label for="userEmail">Email:</label>
        <input type="email" id="userEmail" name="email" required>

        <!-- Password Input -->
        <label for="userPwd">Password:</label>
        <input type="password" id="userPwd" name="password" minlength="8">
    </fieldset>

    <fieldset>
        <legend>Preferences</legend>

        <!-- Radio Buttons -->
        <p>Preferred Contact Method:</p>
        <input type="radio" id="contactEmail" name="contact_method" value="email" checked>
        <label for="contactEmail">Email</label><br>
        <input type="radio" id="contactPhone" name="contact_method" value="phone">
        <label for="contactPhone">Phone</label>

        <!-- Checkbox -->
        <input type="checkbox" id="newsletter" name="subscribe_newsletter" checked>
        <label for="newsletter">Subscribe to newsletter</label>

        <!-- Dropdown (Select) -->
        <label for="country">Country:</label>
        <select id="country" name="country">
            <option value="">--Please choose an option--</option>
            <option value="usa">United States</option>
            <option value="can">Canada</option>
            <option value="mex">Mexico</option>
        </select>

        <!-- Textarea -->
        <label for="comments">Comments:</label>
        <textarea id="comments" name="comments" rows="4" cols="50" placeholder="Your comments here..."></textarea>
    </fieldset>

    <!-- Buttons -->
    <button type="submit">Submit Information</button>
    <button type="reset">Reset Form</button>
</form>
```

## 6. Attributes

Attributes provide additional information about HTML elements.

*   `id="uniqueID"`: Specifies a unique ID for an HTML element.
*   `class="className"`: Specifies one or more class names for an HTML element, used for CSS styling and JavaScript manipulation.
*   `style="property:value;"`: Specifies an inline CSS style for an element.
*   `src="path/to/image.jpg"`: Specifies the URL of the image for `<img>` tags.
*   `href="url"`: Specifies the URL of the page the link goes to for `<a>` tags.
*   `alt="description"`: Specifies an alternate text for an image, if the image cannot be displayed.
*   `width="pixels"` `height="pixels"`: Specifies the width and height of an image or video.
*   `target="_blank"`: Opens the linked document in a new window or tab.
*   `disabled`: Specifies that an input element should be disabled.
*   `checked`: Specifies that an `<input type="checkbox">` or `<input type="radio">` element should be pre-selected.
*   `selected`: Specifies that an option should be pre-selected when the page loads.
*   `placeholder="text"`: Provides a hint to the user about what kind of input is expected.
*   `required`: Specifies that an input field must be filled out before submitting the form.

---

## See Also

-   **[CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md)** - Styling your HTML
-   **[CSS Layout Guide](../guides/CSS_Layout_Guide.md)** - Structuring pages with Flexbox and Grid
-   **[JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md)** - Scripting
-   **[Portfolio Web Development Guide](../guides/Portfolio_Web_Development_Guide.md)** - Practical guide to building a web portfolio