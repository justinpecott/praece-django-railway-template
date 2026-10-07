# Project context
Small internal POC app. Users are non-technical and describe features in plain language.
Keep everything simple and boring.

## Stack (do not deviate)
- Django + Postgres, deployed on Railway (folder is linked to the Railway project)
- Server-rendered Django templates; HTMX only if interactivity is needed. No JS frameworks.
- Django admin is the default back-office UI.
- uv for dependencies, ruff for lint/format.
- Locally: SQLite when DATABASE_URL is unset. In Railway: Postgres via DATABASE_URL.

## Workflow
- Make the change, run `ruff check --fix` and `ruff format`, run migrations locally, verify it works.
- Commit with a plain-English message and push to main. Railway auto-deploys on push.
- After pushing, check deployment status and logs with Railway and report the live URL.
- If a deploy fails, read the logs and fix it before doing anything else.

## Rules
- Before any migration that drops or renames a column or table, explain what data would be lost and wait for a yes.
- Never delete Railway services, volumes, or environments. Never add a public TCP proxy to Postgres.
- Never print secrets or environment variable values.
- Fake data only. Never load real customer data.
- Explain what you did in plain language, without jargon.