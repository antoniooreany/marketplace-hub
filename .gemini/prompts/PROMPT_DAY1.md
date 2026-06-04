# Prompt Day 1

Use `GEMINI.md` as the main operating context.

## Goal for Day 1
Build a runnable foundation and backend MVP for Marketplace Hub Lite.

The project should already start showing:
- Flask API structure
- realistic domain entities
- product, integration, sync, billing, and webhook concepts
- portfolio relevance to a Python + Flask + React SaaS integrations role

## Day 1 workflow
Complete the work in three steps.

### Step 1 — Skeleton validation
Review the existing project skeleton and improve it only if necessary so that the project structure is coherent and runnable.

Confirm or improve:
- backend app factory
- config
- extensions
- blueprint registration
- `/api/v1/health`
- frontend routing shell
- docker-compose
- env examples
- README starter structure

Do not introduce major rewrites if the skeleton is already acceptable.

### Step 2 — Backend MVP
Implement the backend MVP only.

Add or complete:
- database models
- migrations-ready structure
- core service layer
- API routes
- structured JSON responses and errors

Implement these entities:
- User
- Workspace
- Product
- Integration
- SyncJob
- Subscription
- WebhookEvent

Implement these API areas under `/api/v1/`:
- health
- products
- integrations
- sync-jobs
- subscription
- webhook-events
- debug

Domain requirements:
- products: title, sku, price, quantity, status
- integrations: amazon, ebay, shopify, wix
- sync job statuses: queued, running, success, failed
- subscription plans: Free, Pro
- Free plan limits:
  - max 20 products
  - max 1 integration
  - max 5 syncs/day
- enforce at least one backend plan limit
- webhook events should store event_type, payload, status, correlation_id
- include correlation IDs where relevant

### Step 3 — Demo data and local usability
Add:
- seed script
- demo data
- local run instructions
- sample curl commands
- simple mock sync simulation for success/failure cases

Seed requirements:
- 1 demo user
- 1 workspace
- 10 products
- 4 integrations
- 5 sync jobs with mixed statuses
- 1 subscription
- 4 webhook events

## Constraints
- Keep the project runnable at every step
- Do not work on real frontend business pages yet unless small API type adjustments are required
- Keep the backend clean and interview-friendly
- Prefer simple realistic implementation over overengineering

## Expected output format
For each step:
1. Briefly explain the plan
2. Generate or update files
3. Show all created or modified files
4. Explain what changed
5. List anything intentionally unfinished

At the end:
- Show all created or modified files
- Briefly explain what changed
- List remaining backend gaps for Day 2