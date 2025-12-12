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
    --primary-color: rgb(255, 133, 68);
    --secondary-color: rgb(255, 251, 246);
    --accent-color: rgb(255, 192, 158);
}

/* Universal box-sizing */
*, *::before, *::after {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}

body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: var(--secondary-color);
    color: black;
}

/* NAVBAR */
header {
    background-color: black;
    padding: 0 10vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: white;
    height: 7vh;
    border-bottom: 1px solid gray;
}

.nav-links {
    width: 60%;
    display: flex;
    justify-content: space-around;
    list-style: none;
    margin: auto 0;
}

.nav-link {
    text-decoration: none;
    color: grey;
}

.nav-link:hover {
    color: var(--primary-color);
}

.logo {
    color: var(--primary-color);
}
```

### Home Page Specific Styles (`styles/home.css`)
Styles unique to the landing page, often focusing on the hero section layout and responsiveness.
*   **Hero Section:** Centering content, background images, large typography.
*   **Section Layout:** Using Flexbox or Grid for arranging preview content.

```css
.intro {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 85%;
    padding: 7vh 0;
    gap: 40px;
}

.intro-text {
    color: white;
    height: 30vh;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.my-img {
    min-width: 200px;
    height: 200px;
    object-fit: cover;
    object-position: top;
    border-radius: 50%;
    border: 3px solid var(--primary-color);
}

#my-name {
    color: var(--primary-color);
    font-family: monospace;
    font-size: 40px;
}

.btn-shape {
    height: 40px;
    padding: 0 30px;
    border-radius: 7px;
    font-size: 15px;
    font-family: monospace;
    border: none;
}

.intro-btns {
    display: flex;
    gap: 20px;
}

.btn-orange {
    background-color: var(--primary-color);
    color: var(--secondary-color);
}

.btn-hollow {
    background-color: black;
    color: var(--secondary-color);
    border: 1px solid var(--secondary-color);
}

.btn-orange:hover {
    background-color: var(--accent-color);
    color: black;
}

.btn-hollow:hover {
    background-color: var(--accent-color);
    color: black;
}
```

### About Page Specific Styles (`styles/about.css`)
Styles for the about section, potentially using multi-column layouts.

```css
body{
  background-color: black;
}
```

---

## 4. Responsive Design

Ensure the portfolio is viewable on various devices by using media queries. This example shows how to handle a responsive navbar.

```css
/* Example from styles/styles.css */
@media (max-width: 780px) {
  .intro {
    flex-direction: column-reverse;
    align-items: start;
    justify-content: space-between;
    width: 100%;
    padding: 7vh 0;
  }
  .my-img {
    min-width: 150px;
    height: 150px;
  }

  /* Menu Icon for Mobile */
  .menu-icon {
    display: block;
    font-size: 30px;
  }

  /* Hide default nav links */
  .nav-links {
    position: absolute;
    top: 7vh;
    left: 0;
    width: 100%;
    flex-direction: column;
    align-items: center;
    display: none;
    background-color: rgba(255, 255, 255, 0.333);
    border-radius: 0 0 10px 10px;
  }

  .nav-links li {
    padding: 15px 0;
  }

  .nav-link {
    color: white;
  }

  /* When checkbox is checked, show menu */
  #menu-toggle:checked + .menu-icon + .nav-links {
    display: flex;
  }
}
```

### Mobile Menu HTML (for responsive design)
To make the CSS above work, your HTML needs a checkbox hack or JS toggling.

```html
<nav>
    <a href="./index.html"><h2 class="logo">Allan Ahmed</h2></a>
    <!-- Hidden checkbox for toggle state -->
    <input type="checkbox" id="menu-toggle" style="display:none;" />
    <!-- Label acts as the button -->
    <label for="menu-toggle" class="menu-icon">&#9776;</label>
    <ul class="nav-links">
        <li><a href="./index.html" class="nav-link">HOME</a></li>
        <li><a href="./about.html" class="nav-link">ABOUT</a></li>
        <li><a href="" class="nav-link">PROJECTS</a></li>
        <li><a href="" class="nav-link">CONTACT</a></li>
    </ul>
</nav>
```

---

## See Also

-   **[HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md)** - Learn basic and advanced HTML elements.
-   **[CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md)** - Essential CSS properties for styling.
-   **[CSS Layout Guide](../guides/CSS_Layout_Guide.md)** - Master Flexbox and Grid for complex layouts.
-   **[JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md)** - Fundamental JavaScript concepts for interactivity.