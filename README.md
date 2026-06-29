# Enterprise AI Business Intelligence Platform

> Production-grade Business Intelligence platform powered by a Multi-Agent AI Copilot, Semantic Retrieval (RAG), Star Schema Data Warehouse, and enterprise-ready infrastructure — **v1.0.0 Backend MVP**.

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/Mehdiest/Enterprise-AI-Business-Intelligence-Platform)
[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Demo](https://img.shields.io/badge/Watch-Demo-red?logo=loom)](YOUR_LOOM_LINK_HERE)

---

## Overview

The **Enterprise AI Business Intelligence Platform** is a full-stack, production-ready BI system that gives organizations intelligent, natural-language access to their data. A multi-agent AI Copilot interprets business questions, classifies intent, builds context via semantic retrieval, executes a planning pipeline, and delivers cited, confidence-scored answers — all backed by a PostgreSQL star schema warehouse, a pluggable LLM provider layer, and a Docker-based production runtime.

---

## Architecture

```
                 ┌──────────────────────────┐
                 │      REST API / UI       │
                 └────────────┬─────────────┘
                              │
                       FastAPI Gateway
                              │
      ┌───────────────────────┼────────────────────────┐
      │                       │                        │
 Dashboard API          AI Copilot API          Monitoring
      │                       │
      │                Intent Classification
      │                       │
      │               Context Builder (RAG)
      │                       │
      │                 Planner Agent
      │                       │
      │               Execution Engine
      │                       │
      │    ┌──────────────┬──────────────┬─────────────┐
      │    │              │              │
      │ Retriever     SQL Agent     Analytics Agent
      │    │              │              │
      │    └──────────────┴──────────────┘
      │                       │
      │                 Prompt Builder
      │                       │
      │                LLM Provider Layer
      │                       │
      └─────────────── Response Generation
```

---

## Multi-Agent Pipeline

```
User Question
      │
      ▼
Intent Classification
      │
      ▼
Context Builder
      │
      ▼
Planner Agent
      │
      ▼
Execution Engine
      │
      ├── Retriever Agent
      ├── SQL Agent
      ├── Analytics Agent
      └── Response Agent
      │
      ▼
Prompt Builder
      │
      ▼
LLM Provider
      │
      ▼
Enterprise Response
```

---

## Features

### Enterprise AI Copilot
- Rule-based intent classification and context building
- Semantic Retrieval via persistent FAISS vector store (RAG)
- Multi-agent pipeline: Planner → Execution Engine → Agent Registry
- Runtime Execution Context for stateful query handling
- Prompt Builder with enterprise prompt engineering
- Hallucination guard, citation engine, and confidence scoring
- Extensible Agent Registry (Retriever, SQL, Analytics, Response)

### AI Provider Layer
- **Provider Abstraction** — unified LLM interface, provider factory, development mock provider
- Future-ready for OpenAI, Azure OpenAI, Anthropic, Ollama, and local enterprise models — no application logic changes required

### Business Intelligence
- Enterprise KPI engine with executive AI summaries
- Sales narrative generator and forecasting engine
- Customer, product, and regional analytics
- Warehouse aggregations and dashboard APIs

### Data Platform
- ETL pipeline with automated data cleaning
- PostgreSQL star schema warehouse (fact_sales + 5 dimension tables)
- SQLAlchemy 2.0 ORM with Alembic migrations

### Enterprise Infrastructure
- Docker + Docker Compose production runtime
- Structured enterprise logging and health monitoring
- Request ID, timing, and global exception middleware
- Health, ready, and live endpoints
- Feature flags and environment separation

---

## Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python 3.12, FastAPI, SQLAlchemy, Pydantic v2, Alembic, Uvicorn |
| **AI / ML** | Multi-Agent Architecture, Sentence Transformers, FAISS, RAG, Provider Pattern |
| **AI Execution** | Execution Engine, Context Runtime, Planner, Prompt Builder |
| **Data** | PostgreSQL, Star Schema, Pandas, NumPy, Scikit-Learn |
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
│   │   │   │   ├── context/
│   │   │   │   ├── context_runtime/
│   │   │   │   ├── executor/
│   │   │   │   ├── intent/
│   │   │   │   ├── planner/
│   │   │   │   └── prompt/
│   │   │   ├── providers/
│   │   │   ├── retrieval/
│   │   │   ├── vector_store/
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

# Install dependencies
pip install -r requirements/base.txt
```

### Docker Setup

```bash
# Start all services with Docker Compose
docker compose up --build

# Run in background
docker compose up -d --build

# Stop services
docker compose down
```

### Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/bi_platform
OPENAI_API_KEY=your_openai_api_key
ENVIRONMENT=development
LOG_LEVEL=INFO
```

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/copilot/query` | POST | Natural language query via AI Copilot |
| `/api/v1/analytics/kpi` | GET | Enterprise KPI metrics |
| `/api/v1/analytics/forecast` | GET | Sales forecasting |
| `/api/v1/analytics/summary` | GET | Executive AI summary |
| `/api/v1/analytics/customers` | GET | Customer analytics |
| `/api/v1/analytics/products` | GET | Product analytics |
| `/api/v1/analytics/regions` | GET | Regional analytics |
| `/health` | GET | Health check |
| `/ready` | GET | Readiness probe |
| `/live` | GET | Liveness probe |

### Example Request

```bash
curl -X POST http://localhost:8000/api/v1/copilot/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the top 5 products by revenue this quarter?"}'
```

### Example Response

```json
{
  "answer": "The top 5 products by revenue this quarter are...",
  "confidence": 0.92,
  "citations": ["fact_sales", "dim_product"],
  "sql_executed": "SELECT ...",
  "agent_trace": ["planner", "sql_agent", "response_agent"]
}
```

---

## Roadmap

| Version | Status | Highlights |
|---|---|---|
| **v1.0.0** | ✅ Released | Backend MVP — AI Copilot, Multi-Agent Pipeline, Semantic Retrieval, Provider Abstraction, Docker |
| **v1.1.0** | 🔜 Planned | Live SQL Tool Calling, Real RAG Knowledge Base, Conversation Memory |
| **v1.2.0** | 🔜 Planned | Streaming Responses, Multi-Provider Routing, Agent Orchestration |
| **v2.0** | 🔭 Vision | Autonomous Decision Intelligence |

---

## Screenshots

> Demo GIF and screenshots coming soon. Watch the [Loom demo](YOUR_LOOM_LINK_HERE) for a live walkthrough.

---

## Contributing

Contributions, issues, and feature requests are welcome. Please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

> Built with production standards in mind — designed to scale from a single deployment to an enterprise-grade AI decision intelligence infrastructure.
