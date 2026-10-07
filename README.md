## Praece Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)

### Running locally

```sh
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Without `DATABASE_URL` set, the app uses a local SQLite file (`db.sqlite3`).
On Railway, migrations run automatically before each deploy.

Lint and format: `uv run ruff check --fix . && uv run ruff format .`
