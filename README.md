# Marketplace Hub Lite

Marketplace Hub Lite is a production-minded, portfolio-ready full-stack SaaS demo, simulating a merchant dashboard for managing products across multiple e-commerce marketplaces.

## 🚀 Features
- **Product Management:** CRUD operations with subscription plan validation.
- **Marketplace Integrations:** Mock connectors for Amazon, eBay, Shopify, and Wix.
- **Sync Workflow:** Background task handling with status observability and error logging.
- **Webhooks:** System for ingestion and audit logging of marketplace events.
- **Debugging & Ops:** Observability tooling with correlation IDs for tracing.

## 🛠 Tech Stack
- **Backend:** Python, Flask (App Factory pattern), SQLAlchemy (ORM), Alembic (Migrations).
- **Frontend:** React, TypeScript, Vite.
- **DevOps:** Docker, Docker Compose, GitHub Actions.

## 📦 Quick Start
1. Ensure Docker is installed.
2. Clone the repository.
3. Start the project:
   ```bash
   docker-compose up --build
   ```
4. Seed the database with demo data:
   ```bash
   docker-compose exec backend python seed.py
   ```

## 🧪 Testing
The project includes automated testing:
- **Backend:** `pytest backend/tests`
- **Frontend:** `npm test` (via Vitest)

## 🏗 Architecture
- **App Factory Pattern:** Used for scalability and code cleanliness.
- **Service Layer:** Business logic is decoupled from API routes into a centralized `AppService` layer.
- **Strict Typing:** Uses type hints (SQLAlchemy Mapped, TypedDict) for static analysis, improving code reliability and maintainability.
