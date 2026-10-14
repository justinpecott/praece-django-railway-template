## Praece Django Template

### Running locally

```sh
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Without `DATABASE_URL` set, the app uses a local SQLite file (`db.sqlite3`).
On Railway, migrations run automatically before each deploy.

On Railway, the service needs `DATABASE_URL` (reference to Postgres) and `SECRET_KEY`
(a long random value, e.g. `${{secret(50)}}`). See `.env.example`.

Lint and format: `uv run ruff check --fix . && uv run ruff format .`
