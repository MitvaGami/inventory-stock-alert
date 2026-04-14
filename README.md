# Inventory & Stock Alert System

> A FastAPI-based DevOps project demonstrating CI/CD, containerization,
> and automated deployment for a real-world inventory management service.

---

## Problem Statement

Small and mid-size businesses frequently suffer stock-outs or overstock
situations due to lack of real-time inventory visibility. Manual tracking
is error-prone and does not scale. This project implements an automated
**Inventory & Stock Alert System** that tracks product quantities, triggers
low-stock alerts when inventory falls below a configurable threshold, and
generates summary reports — all exposed via a REST API.

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

| Layer | Tool |
|---|---|
| Language | Python 3.11 |
| Web Framework | FastAPI + Uvicorn |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Deployment | Render.com (cloud) |
| Version Control | Git + GitHub |

---

## DevOps Pipeline
Code Push → GitHub → GitHub Actions CI → pytest → Docker Build → Deploy to Render
---

## Project Structure
inventory-stock-alert/
├── app/
│   ├── init.py
│   ├── main.py          # FastAPI app + all endpoints
│   ├── models.py        # Product & Alert data models
│   └── alerts.py        # Low-stock threshold logic
├── tests/
│   ├── test_inventory.py
│   ├── test_alerts.py
│   └── test_reports.py
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions CI pipeline
├── Dockerfile
├── requirements.txt
└── README.md
---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/products` | List all products |
| POST | `/products` | Add a new product |
| PUT | `/products/{id}` | Update product stock |
| DELETE | `/products/{id}` | Remove a product |
| GET | `/alerts` | Get all low-stock alerts |
| GET | `/report` | Generate inventory summary report |

---

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs (auto-generated Swagger UI)

---

## Course Information

- **Course**: 20PECE 601A — DevOps Fundamentals
- **Semester**: II, 2025–2026
- **Institution**: Cummins College of Engineering for Women, Pune
- **Course Outcomes Addressed**: CO1, CO3, CO4