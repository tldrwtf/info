# CI/CD Pipeline Guide

This guide covers setting up Continuous Integration and Continuous Deployment (CI/CD) pipelines for Full Stack applications (Flask Backend + React Frontend) using GitHub Actions.

## 1. Core Concepts

*   **Continuous Integration (CI):** Frequently merging code changes into a central repository. Automated builds and tests run to verify the code quality before it's merged.
*   **Continuous Deployment (CD):** Automatically deploying code to a production environment (like Vercel, Heroku, or AWS) after it passes CI.
*   **GitHub Actions:** A platform within GitHub to automate these workflows.

## 2. Backend CI: Flask & Python

For a Python API, the primary goal of CI is to ensure that new code doesn't break existing functionality. This is achieved by running automated unit tests.

### 2.1. Prerequisites

Ensure your project has a `requirements.txt` and tests written using `unittest` or `pytest`.

**Example Test (`tests/test_add.py`):**
```python
import unittest
from app import app

class TestAddEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_successful_request(self):
        payload = {'num1': 30, 'num2': 20}
        response = self.app.post('/add', json=payload)
        self.assertEqual(response.status_code, 200)
```

### 2.2. GitHub Actions Workflow

Create a file at `.github/workflows/python-ci.yaml`:

```yaml
name: Flask Backend CI

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set Up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
        
      - name: Create Virtual Environment
        run: |
          python -m venv venv
          source venv/bin/activate

      - name: Install dependencies
        run: |
          python -m pip install -U pip
          python -m pip install -r requirements.txt
      
      - name: Run Tests
        # Runs all tests in the 'tests' directory matching 'test_*.py'
        run: |
          source venv/bin/activate
          python -m unittest discover -s tests -p 'test_*.py'
```

---

## 3. Frontend CI/CD: React, Vite & Vercel

For the frontend, CI involves checking for build errors and linting issues. CD involves deploying the optimized build to a hosting provider like Vercel.

### 3.1. Handling Environment Variables (Secrets)

**Security Rule:** NEVER commit `.env` files. Use GitHub Secrets.

In your React app (Vite), you access variables via `import.meta.env` (or `process.env` if using a compatibility plugin).

**GitHub Actions Configuration:**
You must map GitHub Repository Secrets to environment variables in your workflow.

### 3.2. GitHub Actions Workflow

Create a file at `.github/workflows/react-ci-cd.yaml`:

```yaml
name: React Frontend CI/CD

env:
  # Map GitHub Secrets to Environment Variables available during build
  VITE_APP_API_KEY: ${{ secrets.VITE_APP_API_KEY }}
  VITE_APP_AUTH_DOMAIN: ${{ secrets.VITE_APP_AUTH_DOMAIN }}
  VITE_APP_PROJECT_ID: ${{ secrets.VITE_APP_PROJECT_ID }}

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    name: Continuous Integration
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm install --legacy-peer-deps

      - name: Lint Code
        run: npm run lint

      - name: Build Project
        # Ensure build succeeds before deploying
        run: npm run build

  deploy:
    name: Continuous Deployment
    runs-on: ubuntu-latest
    needs: build # Only runs if 'build' succeeds
    if: github.ref == 'refs/heads/main' # Only deploy from main branch
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm install --legacy-peer-deps

      - name: Deploy to Vercel
        # Requires Vercel CLI and a Vercel Token (VT_5) in GitHub Secrets
        run: |
          npm install -g vercel
          vercel --prod --yes --token ${{ secrets.VERCEL_TOKEN }}
```

## 4. Environment Variables in Vite

To ensure your environment variables are picked up during the build process defined above:

1.  **Define in GitHub:** Go to Repo Settings -> Secrets and variables -> Actions -> New repository secret.
2.  **Usage in Code:**
    ```typescript
    // firebase.ts
    const firebaseConfig = {
      apiKey: import.meta.env.VITE_APP_API_KEY, // Native Vite
      // OR if using vite-plugin-environment
      apiKey: process.env.VITE_APP_API_KEY
    };
    ```

## 5. TDD & CI Integration

Test-Driven Development (TDD) pairs perfectly with CI.
1.  **Write a failing test** locally.
2.  **Push** to GitHub -> CI fails (Red).
3.  **Write code** to fix the test.
4.  **Push** -> CI passes (Green).

This ensures your "main" branch is always stable and deployable.