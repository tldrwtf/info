# CI/CD Pipeline Guide: Automating with GitHub Actions

Continuous Integration (CI) and Continuous Deployment (CD) are essential practices for modern software development, ensuring that code changes are automatically tested and safely deployed.

---

## 1. Core Concepts

### Continuous Integration (CI)
The practice of frequently merging code changes into a central repository. Each merge triggers an automated build and test sequence to detect errors early.

### Continuous Deployment (CD)
The practice of automatically deploying every change that passes the CI stage to production.

---

## 2. GitHub Actions Fundamentals

GitHub Actions allows you to automate your workflow directly in your GitHub repository.

### Workflow File Structure
Workflows are defined in `.github/workflows/*.yaml` files.

| Component | Description |
| :--- | :--- |
| **Name** | The name of your workflow. |
| **On** | The GitHub event that triggers the workflow (e.g., `push`, `pull_request`). |
| **Jobs** | A group of steps that run on the same runner (e.g., `ubuntu-latest`). |
| **Steps** | Individual tasks (running a command or using an "Action"). |

---

## 3. Example: Flask CI Pipeline

This workflow automates environment setup, dependency installation, and testing for a Flask application.

```yaml
name: Flask Testing CI

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4 # Downloads your repo code

      - name: Set Up Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.11 # Matches your development environment
        
      - name: Create Virtual Environment
        run: |
          python -m venv venv
          source venv/lib/activate

      - name: Install Dependencies
        run: |
          python -m pip install -U pip
          python -m pip install -r requirements.txt
      
      - name: Run Tests
        # Runs all files matching 'test_*.py' in the 'tests' directory
        run: python -m unittest discover -s tests -p 'test_*.py'
```

---

## 4. Handling Environment Variables

Secrets (like API keys) should never be committed to YAML files. Use **GitHub Secrets**.

1.  Go to `Settings > Secrets and variables > Actions` in your repo.
2.  Add a secret (e.g., `DATABASE_URL`).
3.  Reference it in your workflow:

```yaml
      - name: Run App with Secrets
        env:
          DB_URL: ${{ secrets.DATABASE_URL }}
        run: python app.py
```

---

## 5. Integrating with TDD

CI/CD is most effective when paired with **Test-Driven Development (TDD)**.

1.  **Write a Test:** Define the expected behavior (e.g., a test for a new `/login` route).
2.  **Push to GitHub:** The CI pipeline runs and **fails** (because the feature isn't implemented).
3.  **Implement Code:** Write the logic to make the test pass.
4.  **Push Again:** The CI pipeline runs and **passes**.

---

## See Also

- **[Python API Testing Guide](Python_API_Testing_Guide.md)** - Deep dive into writing the tests that run in this pipeline.
- **[Testing and Debugging Cheat Sheet](../cheatsheets/Testing_and_Debugging_Cheat_Sheet.md)** - Quick reference for `unittest` and `pytest` syntax.
