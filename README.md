# 📦 Inventory & Stock Alert System

> A FastAPI-based DevOps project demonstrating CI/CD, containerization, and automated deployment for a real-world inventory management service.
> ✅ Live, containerized, CI/CD-enabled system deployed on cloud

---

## 🚀 Live Demo

* 🌐 App: https://inventory-stock-alert.onrender.com
* 📘 API Docs: https://inventory-stock-alert.onrender.com/docs
* 🖥️ Dashboard: https://inventory-stock-alert.onrender.com/static/index.html

---

## Problem Statement

Small and mid-size businesses frequently suffer stock-outs or overstock situations due to lack of real-time inventory visibility. Manual tracking is error-prone and does not scale. This project implements an automated **Inventory & Stock Alert System** that tracks product quantities, triggers low-stock alerts when inventory falls below a configurable threshold, and generates summary reports — all exposed via a REST API.

---

## Objectives

1. Build a RESTful inventory service using **FastAPI (Python)**
2. Implement **automated low-stock alert logic** with configurable thresholds
3. Write **automated tests** using pytest to validate business logic
4. Set up a **CI/CD pipeline** using GitHub Actions for build and test automation
5. **Containerize** the application using Docker for environment consistency
6. **Deploy** the service to a cloud staging environment (Render.com)

---

## Tech Stack

| Layer            | Tool               |
| ---------------- | ------------------ |
| Language         | Python 3.9         |
| Web Framework    | FastAPI + Uvicorn  |
| Testing          | pytest             |
| CI/CD            | GitHub Actions     |
| Containerization | Docker             |
| Deployment       | Render.com (cloud) |
| Version Control  | Git + GitHub       |

---

## 🔁 DevOps Pipeline

```
Code Push → GitHub → GitHub Actions → Run Tests (pytest) → Build Docker Image → Deploy to Render
```

---

## 📊 Architecture

```
        ┌──────────────────────┐
        │   Frontend (HTML/JS) │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │   FastAPI Backend    │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Business Logic Layer │
        │ (Alerts, Reports)    │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │   Docker Container   │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │  Render Deployment   │
        └──────────────────────┘
```

---

## API Endpoints

| Method | Endpoint         | Description                       |
| ------ | ---------------- | --------------------------------- |
| GET    | `/products`      | List all products                 |
| POST   | `/products`      | Add a new product                 |
| PUT    | `/products/{id}` | Update product stock              |
| DELETE | `/products/{id}` | Remove a product                  |
| GET    | `/alerts`        | Get all low-stock alerts          |
| GET    | `/report`        | Generate inventory summary report |

---

## 🐳 Docker

```bash
docker build -t inventory-app .
docker run -p 8000:8000 inventory-app
```

---

## 🧪 Testing

```bash
pytest
```

---

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs (auto-generated Swagger UI)

---

## Course Information

* **Course**: 20PECE 601A — DevOps Fundamentals
* **Semester**: II, 2025–2026
* **Institution**: Cummins College of Engineering for Women, Pune
* **Course Outcomes Addressed**: CO1, CO3, CO4

