# Prompt Day 3

Use `GEMINI.md` as the main operating context.

## Goal for Day 3
Turn Marketplace Hub Lite from a working demo into a portfolio-ready, production-minded project.

The result should strongly showcase:
- debugging mindset
- failure handling
- billing enforcement
- testing discipline
- clear documentation
- recruiter-ready presentation

## Day 3 workflow
Complete the work in four steps.

### Step 1 — Failure scenarios and ops realism
Add realistic production-like failure scenarios.

Implement or improve:
1. failed sync due to validation error
2. failed sync due to simulated provider rate limit
3. failed webhook processing
4. subscription downgrade enforcement

Requirements:
- structured error payloads
- timestamps
- correlation IDs
- retry behavior
- last_error fields where relevant
- provider adapter abstraction if justified
- frontend visibility of failure states in:
  - Sync Jobs
  - Billing
  - Webhooks
  - Debug Ops

### Step 2 — Testing
Add a focused but credible test suite.

Backend tests should cover:
- product creation service
- at least one Free plan limit
- sync retry behavior
- webhook persistence or processing result

Frontend tests should cover:
- Products page renders fetched data
- Integrations page connect/disconnect flow
- Billing page shows current plan
- Debug Ops page renders failed jobs

Requirements:
- keep tests small and meaningful
- avoid snapshot spam
- prefer behavior-focused tests

### Step 3 — Documentation and portfolio packaging
Create or improve the README so it becomes portfolio-ready.

README should include:
- project overview
- why this project exists
- relevance to SaaS integrations companies
- tech stack
- architecture overview
- domain entities
- API overview
- key flows
- billing and limits
- mock integrations strategy
- failure and debug flows
- setup steps
- seed instructions
- test commands
- future improvements

Also add:
- 6 strong CV bullet points
- 5 interview talking points
- 3 recruiter-friendly LinkedIn sentences
- suggested screenshots for portfolio presentation

### Step 4 — Final cleanup
Do a cleanup pass across backend and frontend.

Check for:
- inconsistent naming
- duplicate code
- dead imports
- weak UI text
- inconsistent API response shapes
- rough empty/loading/error states
- missing type hints
- missing TypeScript types
- README inconsistencies

Fix issues without adding major new features.

## Constraints
- Keep the project runnable at every step
- Focus on quality, consistency, and presentation
- Do not add unrelated features
- Be honest about remaining gaps

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
- List any remaining gaps honestly