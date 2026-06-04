# Prompt Day 2

Use `GEMINI.md` as the main operating context.

## Goal for Day 2
Build the React frontend MVP and connect it to the backend so the project becomes demoable as a mini SaaS dashboard.

The result should clearly demonstrate:
- React dashboard development
- realistic CRUD and workflow UI
- integration and billing flows
- debug/ops visibility
- clean professional SaaS presentation

## Day 2 workflow
Complete the work in three steps.

### Step 1 — Frontend foundation
Implement or refine the frontend foundation.

Add or improve:
- app shell
- sidebar
- top bar
- route configuration
- shared layout primitives
- typed API client
- core DTO/type definitions

Pages required:
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

Shared UI required:
- PageHeader
- StatCard
- EmptyState
- ErrorState
- LoadingState
- StatusBadge

### Step 2 — Connect product workflows
Implement real data integration for:
- Products page
- Integrations page
- Sync Jobs page

Requirements:
- Products:
  - fetch list
  - create
  - edit
  - delete
  - loading/empty/error states
- Integrations:
  - list integrations
  - connect/disconnect
  - show status, last sync, provider
- Sync Jobs:
  - list jobs
  - create sync job
  - retry failed job
  - show status badges
  - show correlation ID
  - show failure summary

### Step 3 — Billing, webhooks, debug UX
Implement:
- Billing page
- Webhooks page
- Debug Ops page
- Dashboard overview KPIs

Requirements:
- Billing:
  - current plan
  - plan limits
  - upgrade action
  - backend error display when limits are hit
- Webhooks:
  - list webhook events
  - show type, status, timestamp, correlation ID
- Debug Ops:
  - list failed syncs
  - show structured error payload
  - retry action
- Dashboard:
  - total products
  - connected integrations
  - sync jobs today
  - failed sync jobs
  - current plan

## UI constraints
- clean SaaS dashboard
- professional and restrained visual style
- no flashy gradients
- no toy UI
- loading, empty, and error states are required
- make debug/ops pages feel like internal tooling

## Technical constraints
- Do not introduce unnecessary frontend libraries
- Prefer local state and straightforward hooks
- Keep components focused and reusable
- Refactor only where needed

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
- List remaining UX or product gaps for Day 3