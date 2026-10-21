# Project context
Small internal POC app. Users are non-technical and describe features in plain language.
Keep everything simple and boring.

## Environment
- You run in Claude Code on the web (a cloud session). uv, ruff, and git are preinstalled.
- Railway access is through the Railway connector tools. There is no Railway CLI here.
- Railway project: <PROJECT NAME>, environment: production, service: <DJANGO SERVICE NAME>.
- Live URL: <LIVE URL>
- If any value above is still a placeholder, look it up with the Railway tools, fill it in, and commit before doing anything else.

## Stack (do not deviate)
- Django + Postgres, deployed on Railway.
- Server-rendered Django templates; HTMX only if interactivity is needed. No JS frameworks.
- Django admin is the default back-office UI.
- uv for dependencies, ruff for lint/format.
- In this session: SQLite (DATABASE_URL is unset). In Railway: Postgres via DATABASE_URL.
- The app must use DATABASE_URL (private network). DATABASE_PUBLIC_URL must never appear in code or commits.
- Railway build/deploy config lives in railway.json. Change it there, not in the dashboard.

## Workflow
- Make the change. Run `ruff check --fix` and `ruff format`, then `python manage.py check` and migrations locally.
- Ship: commit, merge your working branch into main, and push main. Railway auto-deploys from main.
- After pushing, use the Railway tools to watch the deploy until it finishes.
- If the deploy fails, get the logs (use railway-agent to diagnose if needed), fix it, and ship again before doing anything else.
- Errors and tracebacks are logged to stdout. When the live site errors, read the Railway
  runtime logs before guessing.
- /health/ fails if the database is unreachable or migrations are pending. A failed
  healthcheck on deploy means check the pre-deploy (migrate) output first.
- Migrations run in Railway's pre-deploy step (railway.json). Its output may not appear in 
the logs you can read. Don't move migrate into the start command. If /health/ passes,
migrations ran.
- When the deploy succeeds, curl the live URL to confirm it responds, then give the user the URL.

## Rules
- Before any migration that drops or renames a column or table, explain what data would be lost and wait for a yes.
- Only use Railway tools to check deploy status, read logs, and redeploy. Never create, delete, or reconfigure services, databases, variables, or domains unless the user explicitly asks.
- Never print secrets or environment variable values.
- Fake data only. Never load real customer data.
- Explain what you did in plain language, without jargon.
