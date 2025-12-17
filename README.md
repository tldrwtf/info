# Full Stack Learning - Complete Cheat Sheet Collection

[![Maintenance](https://img.shields.io/badge/Maintained%20by-tldrwtf-blue)](https://github.com/tldrwtf)
[![Version](https://img.shields.io/badge/Version-1.3.0-orange.svg)](#changelog)        

If you find this resource useful, please consider leaving a star!

---

## Table of Contents

- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Available Cheat Sheets](#available-cheat-sheets)
- [In-Depth Guides](#in-depth-guides)
- [Real-World Examples](#real-world-examples)
- [Glossary](#glossary)
- [Troubleshooting](#troubleshooting)
- [Versioning](#versioning)
- [Changelog](#changelog)

---

## Quick Start

Clone the repository to get started with the examples and guides locally:

```bash
git clone https://github.com/tldrwtf/info.git
cd info
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
├── GLOSSARY.md                # Definitions of key terms
└── README.md                  # Project documentation
```

---

## Available Cheat Sheets

| Topic               | Description                        | Link                                     |
| ------------------- | ---------------------------------- | ---------------------------------------- |
| **Python Basics**   | Variables, Loops, Functions        | [Link](cheatsheets/Python_Basics_Cheat_Sheet.md)   |
| **Data Structures** | Lists, Dicts, Trees, Graphs        | [Link](cheatsheets/Data_Structures_Cheat_Sheet.md) |
| **OOP**             | Classes, Inheritance, Polymorphism | [Link](cheatsheets/OOP_Cheat_Sheet.md)             |
| **Regex**           | Pattern Matching & Validation      | [Link](cheatsheets/Regex_Cheat_Sheet.md)           |
| **Big O**           | Time & Space Complexity            | [Link](cheatsheets/Big_O_Notation_Cheat_Sheet.md)  |
| **HTML Basics**     | Tags, Structure, Attributes        | [Link](cheatsheets/HTML_Cheat_Sheet.md)            |
| **CSS Basics**      | Selectors, Box Model, Colors       | [Link](cheatsheets/CSS_Cheat_Sheet.md)             |
| **Bootstrap**       | Grid, Components, Utilities        | [Link](cheatsheets/Bootstrap_Cheat_Sheet.md)       |
| **JS Basics**       | Vars, Types, Loops                 | [Link](cheatsheets/JavaScript_Basics_Cheat_Sheet.md)|
| **JS Objects**      | Objects, Arrays, Methods           | [Link](cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md)|
| **SQL & ORM**       | Queries, Joins, SQLAlchemy         | [Link](cheatsheets/SQL_and_SQLAlchemy_Cheat_Sheet.md)|
| **APIs**            | Requests, REST, JSON               | [Link](cheatsheets/APIs_and_Requests_Cheat_Sheet.md)|

---

## In-Depth Guides

Explore complex topics with our detailed guides in the `guides/` directory.

- **Backend Architecture:** [Flask REST API Development](guides/Flask_REST_API_Development_Guide.md), [Production Workflow](guides/Library-Api_Production_Workflow_Guide.md)
- **Frontend Development:** [React Basics](guides/React_Basics_Guide.md), [Modern Ecommerce](guides/Modern_React_Ecommerce_Guide.md)
- **DevOps:** [CI/CD Pipelines](guides/CI_CD_Pipeline_Guide.md), [Docker (Coming Soon)]()
- **Data & Algorithms:** [Algorithms Guide](guides/Algorithms_Guide.md), [Advanced SQL](guides/SQL_Advanced_Queries_Guide.md)

---

## Real-World Examples

- **Library API:** A fully functional REST API for managing a library system. Located in `library_api_code/`.
- **E-Commerce:** (In Progress) A full-stack React/Flask e-commerce application.

---

## Glossary

Confused by a term? Check out our [Glossary of Terms](GLOSSARY.md) for definitions of acronyms and technical jargon used in this repository.

---

## Troubleshooting

Common issues when setting up the projects:

**1. `ModuleNotFoundError` in Python**
   - **Cause:** Virtual environment not activated or dependencies not installed.
   - **Fix:** 
     ```bash
     source venv/bin/activate
     pip install -r requirements.txt
     ```

**2. Flask App Not Starting**
   - **Cause:** Port 5000 might be in use.
   - **Fix:** Run on a different port:
     ```bash
     flask run --port=5001
     ```

**3. Database Connection Errors**
   - **Cause:** Incorrect URI in `config.py` or database service not running.
   - **Fix:** Verify your connection string and ensure your SQL server is active.

---

## Versioning

- **v1.3.0**: Comprehensive documentation overhaul (Glossary, Troubleshooting, Diagrams).
- **v1.2.0**: Added CI/CD and GraphQL guides.
- **v1.1.0**: Added React and Ecommerce guides.
- **v1.0.0**: Initial release with Python/Flask/SQL curriculum.

---

## Changelog

```text
commit v1.3.0
Date:   Wed Dec 17 2025

docs: Comprehensive documentation overhaul

- Created GLOSSARY.md with key technical definitions
- Refined README.md with Contribution Guidelines and Troubleshooting
- Enhanced Flask_REST_API_Development_Guide.md with Mermaid diagrams and curl examples
- Standardized repository navigation and structure
```

```text
commit v1.2.0
Date:   ???

feat: Add DevOps and GraphQL integration modules

- Created guides/CI_CD_Pipeline_Guide.md (GitHub Actions for Flask/React)
- Created guides/GraphQL_Integration_Guide.md (Flask + Graphene)
- Documented environment variable management and secrets
```

```text
commit v1.1.0
Date:   ???

feat: Add Advanced Web and Testing modules

- Created guides/Modern_React_Ecommerce_Guide.md
- Created guides/Python_API_Testing_Guide.md
- Enriched API_Authentication_Guide.md with Spotify example
```

```text
commit v1.0.1
Date:   ???

feat: Add Real-Time and Frontend Basics
- Created guides/Real_Time_Web_Guide.md (WebSockets)
- Created guides/React_Basics_Guide.md
```

```text
commit v1.0.0
Date:   ???

init: Initialize Core CS and Python curriculum

- Ingested Data Structures, Algorithms, and Python Basics content
- Created guides/Algorithms_Guide.md
- Enriched Cheatsheets for Big O and Data Structures
```
