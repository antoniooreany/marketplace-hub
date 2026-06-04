# Initial Prompt

We are starting a new portfolio-ready full-stack project called **Marketplace Hub Lite**.

Use the project instructions from `GEMINI.md` as the main operating rules.

## Goal
Build a small but realistic SaaS demo tailored to a Python + Flask + React role in an e-commerce integrations company.

The project should demonstrate:
- Flask backend APIs
- React dashboard development
- product and integration workflows
- sync job handling
- webhook processing
- billing and subscription logic
- debugging and observability mindset
- Dockerized local development

## Product concept
Marketplace Hub Lite is a merchant dashboard where a user can:
- manage products
- connect mock marketplace integrations
- run sync jobs
- inspect failures
- view webhook events
- manage subscription limits
- use internal debug and ops pages

This should feel like a mini SaaS product, not a toy CRUD app.

## What to do now
Start with the **project skeleton only**.

Do not implement full business logic yet.
Do not build every feature at once.
Do not create giant files.

## Step 1 requirements
Create the starter structure for:
- backend
- frontend
- dockerized local development
- basic project documentation

### Backend starter
Create a Flask backend starter with:
- app factory
- config
- extensions
- blueprint registration
- `/api/v1/health` endpoint
- placeholder modules for:
  - auth
  - products
  - integrations
  - sync_jobs
  - subscriptions
  - webhooks
  - debug_ops

### Frontend starter
Create a React + TypeScript + Vite starter with:
- app shell
- route setup
- sidebar navigation
- placeholder pages for:
  - Login
  - Dashboard
  - Products
  - Integrations
  - Sync Jobs
  - Billing
  - Webhooks
  - Debug Ops
  - Settings
  - Not Found

### Dev environment
Create:
- `docker-compose.yml`
- backend `.env.example`
- frontend `.env.example`
- dependency manifests
- minimal run instructions

### Documentation
Create a README with:
- project overview
- why this project is relevant
- planned modules
- setup steps
- next implementation milestones

## Constraints
- Keep the project runnable at this step
- Prefer small complete files over giant monolithic ones
- Avoid unnecessary abstractions
- Use realistic naming
- Add TODOs only where useful and specific
- Keep the code clean and interview-friendly

## Expected output format
1. Briefly explain the plan
2. Show the proposed folder tree
3. Generate the starter files
4. Show all created or modified files
5. Briefly explain what changed
6. List anything intentionally unfinished

## Important
Stop after the starter skeleton is complete.
Do not start implementing full backend CRUD, billing logic, sync processing, or detailed UI flows yet.