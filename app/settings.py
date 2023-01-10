from os import environ
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR.parent / ".env")

DATABASE_URL = environ.get("DATABASE_URL")
SECRET_KEY = environ.get("SECRET_KEY")
