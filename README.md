# Full Stack Learning - Complete Cheat Sheet Collection

[![Maintenance](https://img.shields.io/badge/Maintained%20by-tldrwtf-blue)](https://github.com/tldrwtf)

If you find this resource useful, please consider leaving a star!

---

## Table of Contents

- [Full Stack Learning - Complete Cheat Sheet Collection](#full-stack-learning---complete-cheat-sheet-collection)
  - [Table of Contents](#table-of-contents)
  - [Quick Start](#quick-start)
  - [Repository Structure](#repository-structure)
  - [Available Cheat Sheets](#available-cheat-sheets)
  - [In-Depth Guides](#in-depth-guides)
  - [Real-World Examples](#real-world-examples)
  - [Practice Assignments](#practice-assignments)
  - [Changelog](#changelog)

---

## Quick Start

Clone the repository to get started with the examples and guides locally:

```bash
git clone https://github.com/tldrwtf/info.git
cd info
```

For the **Library API** project (a complete Flask reference implementation):

```bash
cd library_api_code
pip install -r requirements.txt
python app.py
```

---

## Repository Structure

```
/
├── cheatsheets/               # Core concept cheat sheets (Python, JS, CSS, SQL, etc.)
├── guides/                    # In-depth tutorials (Advanced patterns, Flask, Auth)
├── Practice_Assignments_Compiled.md # Central hub for all coding challenges
├── Practice_Solutions/        # Full solution code for all assignments
├── library_api_code/          # Production-grade Flask Application
│   ├── app/                   # Application factory & blueprints
│   └── tests/                 # Unit testing suite
└── README.md                  # You are here
```

---

## Available Cheat Sheets

| Topic               | Description                        | Link                                     |
| ------------------- | ---------------------------------- | ---------------------------------------- |
| **Python Basics**   | Variables, Loops, Functions        | [Link](cheatsheets/Python_Basics_Cheat_Sheet.md)   |
| **Data Structures** | Lists, Dicts, Sets, Tuples         | [Link](cheatsheets/Data_Structures_Cheat_Sheet.md) |
| **OOP**             | Classes, Inheritance, Polymorphism | [Link](cheatsheets/OOP_Cheat_Sheet.md)             |
| **Regex**           | Pattern Matching & Validation      | [Link](cheatsheets/Regex_Cheat_Sheet.md)           |
| **Big O**           | Time & Space Complexity            | [Link](cheatsheets/Big_O_Notation_Cheat_Sheet.md)  |
| **Decorators**      | Wrappers & Metaprogramming         | [Link](cheatsheets/Decorators_Cheat_Sheet.md)      |
| **Functional Prog** | Lambda, Map, Filter, Reduce        | [Link](cheatsheets/Functional_Programming_Cheat_Sheet.md)|
| **HTML Basics**     | Tags, Structure, Attributes        | [Link](cheatsheets/HTML_Cheat_Sheet.md)            |
| **CSS Basics**      | Selectors, Box Model, Colors       | [Link](cheatsheets/CSS_Cheat_Sheet.md)             |
| **Bootstrap**       | Grid, Components, Utilities        | [Link](cheatsheets/Bootstrap_Cheat_Sheet.md)       |
| **JS Basics**       | Vars, Types, Loops                 | [Link](cheatsheets/JavaScript_Basics_Cheat_Sheet.md)|
| **JS Objects**      | Arrays, Objects, JSON              | [Link](cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md)|
| **JS Functions**    | Arrow funcs, Scope, Callbacks      | [Link](guides/JavaScript_Functions_Guide.md)   |
| **APIs**            | REST, JSON, Requests               | [Link](cheatsheets/APIs_and_Requests_Cheat_Sheet.md)|

_(See file list for full collection)_

---

## In-Depth Guides

For complex topics requiring architectural understanding:

- **[Flask REST API Development](guides/Flask_REST_API_Development_Guide.md)**: Building scalable web APIs.
- **[Library-Api Advanced Architecture](guides/Library-Api_Advanced_Architecture_Guide.md)**: Analysis of the `library_api_code` reference project.
- **[SQLAlchemy Relationships](guides/SQLAlchemy_Relationships_Guide.md)**: Mastering One-to-Many and Many-to-Many patterns.
- **[SQLAlchemy CRUD](guides/SQLAlchemy_CRUD_Guide.md)**: Create, Read, Update, Delete operations in depth.
- **[Advanced SQL Queries](guides/SQL_Advanced_Queries_Guide.md)**: Joins, Subqueries, and Optimization.
- **[API Authentication](guides/API_Authentication_Guide.md)**: Securing apps with JWT and OAuth2.
- **[Python CLI Applications](guides/Python_CLI_Applications_Guide.md)**: Building interactive command-line tools.
- **[Building AI-Ready APIs](guides/Building_AI_Ready_APIs_Guide.md)**: Designing Flask endpoints for consumption by AI agents and tools.
- **[Flask AI Tools Integration](guides/Flask_AI_Tools_Integration_Guide.md)**: Integrating LLMs and AI services into Flask apps.
- **[CSS Layout Guide](guides/CSS_Layout_Guide.md)**: Mastering Flexbox and Grid for modern web layouts.
- **[DOM Manipulation](guides/DOM_Manipulation_Guide.md)**: Interacting with the webpage using JavaScript.
- **[Portfolio Development](guides/Portfolio_Web_Development_Guide.md)**: Building a personal developer portfolio.
- **[JavaScript Workshops](guides/JavaScript_Workshops_Guide.md)**: Practical mini-projects (Color Picker, Shopping Cart, etc.).

---

## Real-World Examples

Explore production-ready code in the `library_api_code/` directory and `Practice_Solutions/` folder:

- **Library API**: Full Flask app with Blueprints, Caching, Rate Limiting, and JWT.
- **Mechanic Shop API**: Service ticket tracking and analytics.
- **Inventory System**: "Item Definition" vs "Physical Instance" pattern.
- **RPG Battle Game**: OOP inheritance and polymorphism demonstration.
- **Spotify Auth**: Client Credentials Flow implementation.

---

## Practice Assignments

Put your knowledge to the test! We have compiled a comprehensive list of coding challenges covering all topics.

- **[Go to Practice Assignments](Practice_Assignments_Compiled.md)**

Each assignment includes:

- Clear objectives.
- Context/Scenario.
- Links to the specific solution file in `Practice_Solutions/`.

---

## Changelog

**2025-12-16 Updates**

- **Documentation:**
    - Created `cheatsheets/Bootstrap_Cheat_Sheet.md` covering Grid, Components, and Utilities.
    - Created `guides/JavaScript_Workshops_Guide.md` with 5 practical mini-projects (DOM, Logic, LocalStorage).
    - Updated `guides/SQLAlchemy_Relationships_Guide.md` with conceptual diagrams and lazy loading performance charts.
    - Updated `guides/Python_CLI_Applications_Guide.md` with packaging/distribution instructions (`setup.py`).
    - Updated `guides/CSS_Layout_Guide.md` with Media Query responsive design patterns.
    - Updated `cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md` with more array methods (`find`, `reduce`).
    - Updated `guides/JavaScript_Functions_Guide.md` with practical exercises.
    - Updated `guides/DOM_Manipulation_Guide.md` with modern selector examples.

- **Curriculum:**
    - Added "Section 16: Web Interactivity & Frameworks" to `Practice_Assignments_Compiled.md`.

- **Maintenance:**
    - Validated internal linking structure across all Markdown files.
    - Standardized headers and formatting across new guides.