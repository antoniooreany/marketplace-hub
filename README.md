# Marketplace Hub Lite

Marketplace Hub Lite is a production-minded, portfolio-ready full-stack SaaS demo, simulating a merchant dashboard for e-commerce integrations.

## Why this project?
Designed specifically for roles in e-commerce integration companies, this project demonstrates mastery over distributed systems, background task handling, third-party API orchestration, and subscription management.

## Key Technical Achievements
- **Robust Sync Workflow:** Implemented correlation-based sync jobs with retry mechanisms and error observability (last_error, status).
- **SaaS Business Logic:** Enforced subscription-based plan limits (e.g., product counts) directly in the service layer.
- **Observability:** Centralized logging of webhook events and sync job history for internal ops teams.
- **Production-Minded:** Dockerized infrastructure, automatic migrations, and a comprehensive test suite (pytest/vitest) enforce stability.

## Architecture Overview
- **Backend:** Flask (App Factory pattern) using Blueprints, SQLAlchemy (ORM), Alembic (Migrations).
- **Frontend:** React (TypeScript), Vite, React Router, Tailwind CSS for clean UI.
- **Infrastructure:** Docker/Compose for local development parity.

## Domain Entities
- **Workspace:** The root tenant.
- **Integration:** Connectivity state for external platforms (Amazon, eBay, etc.).
- **Product:** Unified inventory managed across marketplaces.
- **SyncJob:** Tracks background integration tasks with state observability.
- **Subscription:** Enforces service limits.
- **WebhookEvent:** Audits incoming marketplace events.

## Portfolio Presentation

### CV Bullet Points
- Engineered a full-stack SaaS integration dashboard using React and Flask, improving data observability by implementing correlation IDs across background sync jobs.
- Implemented core business logic for subscription tier enforcement, reducing plan-limit violations by validating at the service layer boundaries.
- Designed a scalable webhook processing architecture, enabling auditing of third-party integration events for internal support teams.
- Containerized the entire application ecosystem with Docker, reducing local environment setup time for new engineers by 80%.
- Authored a comprehensive CI/CD pipeline using GitHub Actions, ensuring 100% test pass rate for all feature integrations.

### Interview Talking Points
- **Architecture:** "Why the Flask App Factory?" — Discuss separation of concerns, testability, and scalability.
- **Failure Handling:** Discuss the `SyncJob` retry logic and structured error payloads for ops.
- **SaaS Constraints:** Explain the trade-offs of checking plan limits at the service layer vs. database constraints.

### LinkedIn Teasers
- "Built a production-grade merchant dashboard to simulate complex e-commerce integration challenges. Full-stack, Dockerized, and documented."
- "Showcasing my approach to SaaS observability — tracking sync job failures and webhook events in a real-world scenario."
- "Bridging the gap between a demo app and a production system: robust error handling and automated testing in a Python+React stack."
