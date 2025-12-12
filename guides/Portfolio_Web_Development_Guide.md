# Portfolio Web Development Guide

This guide outlines the fundamental structure and styling considerations for building a personal portfolio website, drawing examples from a class code example. It focuses on HTML organization and responsive CSS design using Flexbox and Grid concepts.

---

## 1. Project Structure and Overview

A typical portfolio website includes sections like Home, About, Projects, and Contact. Each section is built with semantic HTML and styled with CSS.

### Key Files
*   `index.html`: The main landing page, often featuring a hero section and navigation.
*   `about.html`: Provides details about your skills, experience, and background.
*   `styles/styles.css`: Global styles, typography, and layout for the entire site.
*   `styles/home.css`: Specific styles for the home page.
*   `styles/about.css`: Specific styles for the about page.

---

## 2. HTML Structure

Semantic HTML5 elements are crucial for accessibility and SEO.

### `index.html` - Home Page
Typically includes:
*   **Header:** Navigation (`nav`), logo, main title.
*   **Hero Section:** Prominent introduction with a call to action.
*   **About/Skills Preview:** Short summaries linking to the `about.html` page.
*   **Footer:** Contact information, social links.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="styles/styles.css">
    <link rel="stylesheet" href="styles/home.css">
</head>
<body>
    <header>
        <nav>
            <!-- Navigation links -->
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Welcome to My Portfolio</h1>
            <p>A passionate web developer</p>
            <a href="#projects" class="button">View My Work</a>
        </section>
        <section id="about-preview">
            <!-- Short about me content -->
        </section>
    </main>
    <footer>
        <!-- Footer content -->
    </footer>
</body>
</html>
```

### `about.html` - About Page
Focuses on detailed personal and professional information.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>
    <link rel="stylesheet" href="styles/styles.css">
    <link rel="stylesheet" href="styles/about.css">
</head>
<body>
    <header>
        <nav>
            <!-- Navigation links -->
        </nav>
    </header>
    <main>
        <section id="bio">
            <h2>About Me</h2>
            <p>Detailed biography...</p>
        </section>
        <section id="skills">
            <h3>Skills</h3>
            <ul>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
                <!-- More skills -->
            </ul>
        </section>
    </main>
    <footer>
        <!-- Footer content -->
    </footer>
</body>
</html>
```

---

## 3. CSS Styling and Layout

Effective CSS is key to visual appeal and responsiveness.

### Global Styles (`styles/styles.css`)
This file defines styles that apply across the entire website. This often includes:
*   **Root Variables:** For colors, fonts, spacing.
*   **Typography:** Base font sizes, line heights, font families.
*   **Reset/Normalize:** To ensure consistent rendering across browsers.
*   **Basic Layout:** Styles for `body`, `header`, `nav`, `main`, `footer`.

```css
/* Root Variables */
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --text-color: #333;
    --bg-color: #f4f4f4;
}

/* Universal box-sizing */
*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: var(--bg-color);
    color: var(--text-color);
}

header {
    background-color: var(--primary-color);
    color: white;
    padding: 1rem 0;
}

nav ul {
    list-style: none;
    padding: 0;
    display: flex; /* Flexbox for navigation */
    justify-content: center;
}

nav ul li a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
}
```

### Home Page Specific Styles (`styles/home.css`)
Styles unique to the landing page, often focusing on the hero section layout and responsiveness.
*   **Hero Section:** Centering content, background images, large typography.
*   **Section Layout:** Using Flexbox or Grid for arranging preview content.

```css
#hero {
    background-color: var(--secondary-color);
    color: white;
    text-align: center;
    padding: 4rem 1rem;
    min-height: 80vh; /* Full viewport height */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

#hero h1 {
    font-size: 3em;
    margin-bottom: 0.5rem;
}

.button {
    display: inline-block;
    background-color: var(--primary-color);
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 5px;
    text-decoration: none;
    margin-top: 1rem;
}
```

### About Page Specific Styles (`styles/about.css`)
Styles for the about section, potentially using multi-column layouts.

```css
/* Minimal example */
#bio {
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
}
```

---

## 4. Responsive Design

Ensure the portfolio is viewable on various devices by using media queries.

```css
/* Example from styles/styles.css */
@media (max-width: 768px) {
    nav ul {
        flex-direction: column;
        align-items: center;
    }
    nav ul li {
        margin-bottom: 0.5rem;
    }
    #hero h1 {
        font-size: 2em;
    }
}
```

---

## See Also

-   **[HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md)** - Learn basic and advanced HTML elements.
-   **[CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md)** - Essential CSS properties for styling.
-   **[CSS Layout Guide](../guides/CSS_Layout_Guide.md)** - Master Flexbox and Grid for complex layouts.
-   **[JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md)** - Fundamental JavaScript concepts for interactivity.