# STVRAF Framework

**Sovereign Threat Vector Risk Assessment Framework**

A production-grade REST API backend implementing the **STVRAF** research framework — a Bayesian probabilistic model for assessing and tracking cyber-physical risk across fleet segments. Built with FastAPI, SQLAlchemy, and Pydantic.

---

## 📖 Overview

STVRAF models the probability of a threat event occurring across distinct fleet segments using Bayesian inference. Each segment tracks:

- **Prior probability** `P(A)` — baseline threat likelihood
- **Posterior probability** `P(A|E)` — updated probability after observing telemetry evidence
- **Impact Severity** — consequence weight of a threat
- **Confidence Discount** — reduces score when evidence confidence is low
- **Composite Risk Score** — final weighted risk metric

---

## 🗂️ Project Structure

```
STVRAF_Framework/
├── main.py                  # FastAPI app entry point
├── requirements.txt         # Python dependencies
├── run_tests.py             # Standalone math verification tests
├── api/
│   └── endpoints.py         # REST API routes
├── core/
│   ├── database.py          # SQLAlchemy engine & session
│   └── risk_engine.py       # Bayesian risk calculation logic
├── models/
│   └── fleet_segment.py     # ORM model
├── schemas/
│   └── schemas.py           # Pydantic schemas
└── tests/
    └── test_risk_engine.py  # Unit tests
```

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/RishitJariwala/STVRAF_Framework.git
cd STVRAF_Framework
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Running the API Server

```bash
uvicorn main:app --reload
```

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 🧪 Running Tests

```bash
PYTHONPATH=. python run_tests.py
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/api/v1/segments/` | Create fleet segment |
| GET | `/api/v1/segments/{id}` | Get risk score |
| POST | `/api/v1/telemetry/` | Ingest telemetry & update risk |

---

## 🔬 Risk Engine

```
Composite Risk Score = P(A|E) × Impact Severity × Confidence Discount
P(A|E) = [P(E|A) × P(A)] / P(E)
```

---

## 📄 License

Academic research project. All rights reserved © Rishit Jariwala.
