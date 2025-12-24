# Docker and Containerization Guide

This guide introduces Docker, explaining how to containerize applications for consistent development, testing, and production environments.

---

## 1. What is Docker?

Docker is a platform that uses OS-level virtualization to deliver software in packages called **containers**. Containers are isolated from each other and bundle their own software, libraries, and configuration files.

### Key Benefits
*   **Consistency:** "It works on my machine" becomes "It works everywhere."
*   **Isolation:** Dependencies for one app won't interfere with another.
*   **Efficiency:** Containers share the host OS kernel, making them lightweight.

---

## 2. Core Concepts

| Component | Description |
| :--- | :--- |
| **Dockerfile** | A text file containing instructions to build a Docker Image. |
| **Image** | A read-only template used to create containers. |
| **Container** | A running instance of an image. |
| **Docker Hub** | A registry for sharing and finding Docker images. |

---

## 3. Containerizing a Flask App

Assume we have a Flask app in a directory with a `requirements.txt`.

### Step 1: Create a `Dockerfile`
Create a file named `Dockerfile` (no extension) in your project root.

```dockerfile
# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code
COPY . .

# 5. Expose the port the app runs on
EXPOSE 5000

# 6. Define the command to run the app
CMD ["python", "app.py"]
```

### Step 2: Build the Image
```bash
docker build -t flask-app-demo .
```

### Step 3: Run the Container
```bash
docker run -p 5000:5000 flask-app-demo
```
*The app is now accessible at `http://localhost:5000`.*

---

## 4. Multi-Container Apps with Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications (e.g., Flask + PostgreSQL).

### Example `docker-compose.yml`
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Running the Stack
```bash
docker-compose up -d
```

---

## 5. Common Commands

*   `docker ps`: List running containers.
*   `docker images`: List downloaded/built images.
*   `docker stop <id>`: Stop a container.
*   `docker rm <id>`: Remove a container.
*   `docker rmi <id>`: Remove an image.
*   `docker exec -it <id> bash`: Open a terminal inside a running container.

---

## See Also
- **[CI/CD Pipeline Guide](CI_CD_Pipeline_Guide.md)** - Automating Docker builds with GitHub Actions.
- **[Flask Production Workflow](Library-Api_Production_Workflow_Guide.md)** - Best practices for deploying Flask.
