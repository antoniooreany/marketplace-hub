# Project Instructions

## Project
Marketplace Hub Lite is a portfolio-ready full-stack SaaS demo for a Python + Flask + React role in an e-commerce integrations company.

## Goals
This project should help demonstrate practical, portfolio-relevant experience for roles that expect:
- Python and Flask backend development
- React dashboard development
- REST API design
- third-party integration workflows
- sync job handling
- webhook processing
- billing and subscription logic
- debugging and observability mindset
- Dockerized local development

## Domain
Marketplace Hub Lite is a merchant dashboard for:
- product management
- marketplace integrations (Amazon, eBay, Shopify, Wix)
- sync jobs and retry flows
- subscription limits and upgrade flows
- webhook events
- debug and ops pages

The project should feel like a small but realistic SaaS product used by merchants and internal support/engineering teams.

## Core product direction
Prefer product decisions that make the project look relevant to an e-commerce integrations company:
- integration connection states
- sync job history and retry
- structured errors
- correlation IDs
- subscription plan enforcement
- webhook event visibility
- internal debug and ops tooling

Avoid turning this into a generic todo app, blog, or unrelated CRUD demo.

## Execution rules
- Keep the project runnable at every step
- Prefer small complete files over giant monolithic files
- Do not invent unnecessary abstractions
- Preserve existing working code unless refactoring is necessary
- If you change structure, explain why briefly
- Show all created or modified files after each step

## Scope control
- Do only what is requested in this step
- Do not preemptively implement future features
- Do not rewrite unrelated files
- If a future improvement is tempting, mention it briefly instead of implementing it now
- If the requested scope is too large for one step, propose a smaller implementation slice first

## Clarification rule
- If a task is ambiguous, ask a brief clarifying question before making large structural changes
- If multiple implementation paths are possible, choose the simplest realistic option unless told otherwise

## Architecture preferences
### Backend
- Use Flask app factory pattern
- Use blueprints for API modules
- Use services for business logic
- Use models for persistence
- Use repositories only where they are clearly justified
- Keep the architecture clean and understandable
- Prefer explicit code over clever abstractions
- Use realistic API names, module names, and entity names

### Frontend
- Use React with TypeScript
- Prefer pages, reusable components, feature-level organization, and a simple typed API client
- Prefer local state and straightforward composition unless a stronger state solution is clearly needed
- Keep components focused and maintainable
- Avoid unnecessary frontend libraries

## Coding preferences
- Favor clarity over cleverness
- Keep files concise but production-minded
- Use realistic naming
- Add comments only where they are genuinely useful
- Avoid toy examples unless explicitly requested
- If TODOs are added, make them short, concrete, and actionable
- Prefer code that is easy to explain in an interview

## Backend preferences
- REST endpoints should be consistent and predictable
- Use structured JSON responses
- Use structured JSON errors
- Include timestamps where useful
- Include correlation IDs where relevant for sync jobs, webhook events, and failure flows
- Validate input at API boundaries
- Keep plan limit enforcement on the backend, not only in the UI

## Frontend preferences
- Prefer a clean SaaS dashboard layout
- Use sober, professional styling
- No flashy gradients
- No toy-project styling
- Include loading, empty, and error states where relevant
- Prefer clear tables, cards, filters, and detail views over gimmicky UI
- Make debug and ops views feel like internal tooling, not marketing pages

## UI preferences
- Clean professional SaaS dashboard
- Neutral, restrained visual style
- Consistent spacing and typography
- Reusable status badges and feedback components
- Clear success, error, and disabled states
- Responsive layout without overengineering
- Make the interface easy to demo in screenshots

## Testing preferences
- Add small but meaningful tests
- Prefer behavior-focused tests over snapshots
- Focus tests on business-critical flows
- Good targets include:
  - plan limit enforcement
  - sync retry behavior
  - webhook persistence/processing
  - product CRUD flows
  - integration connect/disconnect flows

## Documentation preferences
- Keep README professional and concrete
- Explain architecture decisions briefly
- Describe domain entities and major flows
- Explain how mock integrations work
- Explain billing and plan limits
- Explain failure scenarios and debug flows
- Include setup, seed, and test instructions
- Include portfolio-ready bullets when asked

## Output preference
For every task:
1. Briefly explain the plan
2. Generate or update files
3. Show all created or modified files
4. Explain what changed
5. List anything intentionally unfinished

At the end:
- Show all created or modified files
- Briefly explain what changed

## Quality bar
Each step should move the project toward a demo-ready state.
A good result is:
- runnable
- understandable
- relevant to the target role
- easy to explain
- easy to extend in the next step

A bad result is:
- overengineered
- partially broken
- full of placeholder boilerplate
- visually toy-like
- unrelated to integrations, billing, sync workflows, or debugging
