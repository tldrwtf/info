# Python Learning - Complete Cheat Sheet Collection

[![Maintenance](https://img.shields.io/badge/Maintained%20by-tldrwtf-blue)](https://github.com/tldrwtf)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

If you find this resource useful, please consider leaving a star!

---

## Table of Contents

- [Python Learning - Complete Cheat Sheet Collection](#python-learning---complete-cheat-sheet-collection)
  - [Table of Contents](#table-of-contents)
  - [Quick Start](#quick-start)
  - [Repository Structure](#repository-structure)
  - [Learning Paths](#learning-paths)
    - [Beginner Path](#beginner-path)
    - [Intermediate Path](#intermediate-path)
    - [Advanced Path](#advanced-path)
  - [Available Cheat Sheets](#available-cheat-sheets)
  - [In-Depth Guides](#in-depth-guides)
  - [Real-World Examples](#real-world-examples)
  - [Practice Assignments](#practice-assignments)

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
├── *_Cheat_Sheet.md           # Core concept cheat sheets (18 files)
├── *_Guide.md                 # In-depth tutorials (Advanced patterns, Flask, Auth)
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
| **Python Basics**   | Variables, Loops, Functions        | [Link](./Python_Basics_Cheat_Sheet.md)   |
| **Data Structures** | Lists, Dicts, Sets, Tuples         | [Link](./Data_Structures_Cheat_Sheet.md) |
| **OOP**             | Classes, Inheritance, Polymorphism | [Link](./OOP_Cheat_Sheet.md)             |
| **Regex**           | Pattern Matching & Validation      | [Link](./Regex_Cheat_Sheet.md)           |
| **Big O**           | Time & Space Complexity            | [Link](./Big_O_Notation_Cheat_Sheet.md)  |
| **Decorators**      | Wrappers & Metaprogramming         | [Link](./Decorators_Cheat_Sheet.md)      |

_(See file list for full collection)_

---

## In-Depth Guides

For complex topics requiring architectural understanding:

- **[Flask REST API Development](./Flask_REST_API_Development_Guide.md)**: Building scalable web APIs.
- **[Library-Api Advanced Architecture](./Library-Api_Advanced_Architecture_Guide.md)**: Analysis of the `library_api_code` reference project.
- **[SQLAlchemy Relationships](./SQLAlchemy_Relationships_Guide.md)**: Mastering One-to-Many and Many-to-Many patterns.
- **[API Authentication](./API_Authentication_Guide.md)**: Securing apps with JWT and OAuth2.
- **[Safe Programming & Secrets](./Library-Api_Production_Workflow_Guide.md#6-safe-programming-environment-variables-and-private-properties)**: Practical tips on handling secrets, environment variables, and class encapsulation.

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

- **[Go to Practice Assignments](./Practice_Assignments_Compiled.md)**

Each assignment includes:

- Clear objectives.
- Context/Scenario.
- Links to the specific solution file in `Practice_Solutions/`.
