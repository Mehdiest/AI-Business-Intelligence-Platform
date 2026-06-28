# Enterprise AI Business Intelligence Platform

> Production-grade Business Intelligence platform powered by a Multi-Agent AI Copilot, Semantic Retrieval (RAG), Star Schema Data Warehouse, and enterprise-ready infrastructure.

---

## Overview

The **Enterprise AI Business Intelligence Platform** is a full-stack, production-ready BI system designed for organizations that need intelligent, natural-language access to their data. At its core, a multi-agent AI Copilot interprets business questions, generates and validates SQL, retrieves semantic context via RAG, and delivers cited, confidence-scored answers — all backed by a PostgreSQL star schema warehouse and a Docker-based production runtime.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      Client Layer                       │
│           REST API (FastAPI)  │  Future Dashboard/SDK   │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│                   Application Layer                     │
│        API Routers │ Middleware │ Dependency Injection  │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│               Enterprise AI Copilot                     │
│   Planner Agent → SQL Agent → Response Agent            │
│             Multi-Agent Orchestration                   │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│              Enterprise Response Layer                  │
│  Formatter │ Citation Engine │ Confidence Engine        │
│  Hallucination Guard │ Response Validator               │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│            Retrieval & Knowledge Layer                  │
│   Context Builder → Semantic Retriever → FAISS DB       │
│                    Embedding Service                    │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│                   Analytics Layer                       │
│  KPI Engine │ Forecast Service │ Executive Summary      │
│  Sales Narrative │ Business Metrics │ Aggregations      │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│                    Data Platform                        │
│  ETL Pipeline │ Data Cleaning │ PostgreSQL Warehouse    │
│               Star Schema │ SQLAlchemy ORM              │
│                                                         │
│  Fact:   fact_sales                                     │
│  Dims:   dim_customer │ dim_product │ dim_region        │
│          dim_channel  │ dim_date                        │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│              Enterprise Infrastructure                  │
│  Docker │ Docker Compose │ Enterprise Logging           │
│  Request ID │ Timing │ Exception Middleware             │
│  Health │ Ready │ Live Endpoints │ Feature Flags        │
└─────────────────────────────────────────────────────────┘
```

---

## Features

### Enterprise AI Copilot
- Multi-agent pipeline: **Planner → SQL → Response**
- Intent classification, context building, prompt engineering
- SQL generation, validation, and execution
- Semantic Knowledge Engine with persistent FAISS vector store
- Retrieval-Augmented Generation (RAG) with citation engine
- Hallucination guard and confidence scoring

### Business Intelligence
- Enterprise KPI engine with executive AI summaries
- Sales narrative generator and forecasting engine
- Customer, product, and regional analytics
- Warehouse aggregations and dashboard APIs

### Data Platform
- ETL pipeline with automated data cleaning
- PostgreSQL star schema warehouse
- SQLAlchemy 2.0 ORM with Alembic migrations

### Enterprise Infrastructure
- Docker + Docker Compose production runtime
- Structured enterprise logging
- Health, ready, and live endpoints
- Request ID, timing, and global exception middleware
- Feature flags and environment separation

---

## Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python 3.12, FastAPI, SQLAlchemy, Pydantic v2, Alembic, Uvicorn |
| **AI / ML** | Sentence Transformers, FAISS, RAG, Multi-Agent Architecture |
| **Data** | PostgreSQL, Pandas, NumPy, Scikit-Learn |
| **Infrastructure** | Docker, Docker Compose, Enterprise Logging, Feature Flags |
| **Dev Tools** | Git, GitHub, Pytest, VS Code |

---

## Project Structure

```
Enterprise-AI-Business-Intelligence-Platform/
├── app/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── middleware/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   │   ├── analytics/
│   │   ├── ai/
│   │   │   ├── copilot/
│   │   │   │   ├── agents/
│   │   │   │   │   ├── planner/
│   │   │   │   │   ├── sql/
│   │   │   │   │   └── response/
│   │   │   │   ├── middleware/
│   │   │   │   ├── prompts/
│   │   │   │   └── shared/
│   │   │   ├── embeddings.py
│   │   │   ├── insights.py
│   │   │   └── semantic_search.py
│   │   └── reporting/
│   ├── warehouse/
│   └── utils/
├── docker/
├── requirements/
├── tests/
└── alembic/
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- PostgreSQL 15+
- OpenAI API key (or compatible LLM provider)

### Installation

```bash
# Clone the repository
git clone https://github.com/Mehdiest/Enterprise-AI-Business-Intelligence-Platform.git
cd Enterprise-AI-Business-Intelligence-Platform

# Copy environment configuration
cp .env.example .env
# Fill in your credentials in .env

# Start with Docker Compose
docker compose up --build
```

### Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/bi_platform
OPENAI_API_KEY=your_openai_api_key
ENVIRONMENT=development
```

---

## API Endpoints

| Endpoint | Description |
|---|---|
| `POST /api/v1/copilot/query` | Natural language query via AI Copilot |
| `GET /api/v1/analytics/kpi` | Enterprise KPI metrics |
| `GET /api/v1/analytics/forecast` | Sales forecasting |
| `GET /api/v1/analytics/summary` | Executive AI summary |
| `GET /health` | Health check |
| `GET /ready` | Readiness probe |
| `GET /live` | Liveness probe |

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

> Built with production standards in mind — designed to scale from a single deployment to an enterprise-grade BI infrastructure.
