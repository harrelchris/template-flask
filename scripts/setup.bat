@echo off

:: Create virtual environment
if not exist .venv\ (
	python -m venv .venv
)

:: Activate virtual environment
if not defined VIRTUAL_ENV (
	call .venv\Scripts\activate
)

:: Update virtual environment
python -m pip install -U pip setuptools wheel

:: Install dependencies
pip install -r requirements-dev.txt

:: Install pre-commit
pre-commit install

:: Create .env from example
if not exist .env (
	copy .env.example .env
)

:: Delete the existing database
if exist db.sqlite3 (
	del db.sqlite3
)

:: Initialize a clean database
alembic -c app/migrations/alembic.ini revision --autogenerate
alembic -c app/migrations/alembic.ini upgrade head

:: Create super user
flask user admin user pass
