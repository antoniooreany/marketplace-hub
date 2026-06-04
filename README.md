# Marketplace Hub Lite

Marketplace Hub Lite is a portfolio-ready full-stack SaaS demo for a Python + Flask + React role in an e-commerce integrations company.

## Project Overview
This project simulates a merchant dashboard for managing products across multiple marketplaces (Amazon, eBay, Shopify, Wix). It demonstrates REST API design, third-party integration workflows, sync job handling, and subscription logic.

## Key Features (Planned)
- **Product Management:** CRUD operations for products.
- **Marketplace Integrations:** Mock connectors for major e-commerce platforms.
- **Sync Jobs:** History, retry logic, and correlation IDs for background tasks.
- **Webhooks:** Inspection of incoming events from marketplaces.
- **Billing & Subscriptions:** Plan limit enforcement and upgrade flows.
- **Internal Debug & Ops:** Tooling for support and engineering teams.

## Tech Stack
- **Backend:** Python, Flask, SQLAlchemy, Flask-Migrate.
- **Frontend:** React, TypeScript, Vite, React Router, Lucide React.
- **Infrastructure:** Docker, Docker Compose.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed.

### Setup
1. Clone the repository.
2. Run `docker-compose up --build`.
3. Backend will be available at `http://localhost:5000`.
4. Frontend will be available at `http://localhost:3000`.

### Initial Milestones
1. [x] Project skeleton (Backend + Frontend + Docker).
2. [ ] Backend: Auth & Product CRUD.
3. [ ] Frontend: Product Dashboard.
4. [ ] Mock Integrations & Sync Jobs.
5. [ ] Webhooks & Billing.

## Why this project?
This project is designed to showcase skills relevant to e-commerce integration roles:
- Handling distributed data (syncing products).
- Managing third-party API states.
- Observability and debugging (sync logs, webhooks).
- Business logic constraints (plan limits).
