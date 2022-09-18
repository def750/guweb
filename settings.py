from __future__ import annotations

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from starlette.datastructures import Secret

config = Config(".env")

APP_NAME = config("APP_NAME")
SECRET_KEY = config("SECRET_KEY", cast=Secret)

DOMAIN = config("DOMAIN")
GULAG_PATH = config("GULAG_PATH")

HCAPTCHA_PUBLIC = config("HCAPTCHA_PUBLIC")
HCAPTCHA_SECRET = config("HCAPTCHA_SECRET", cast=Secret)

DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT", cast=int)
DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS", cast=Secret)
DB_NAME = config("DB_NAME")
DB_DSN = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DISALLOWED_NAMES = config("DISALLOWED_NAMES", cast=CommaSeparatedStrings)
DISALLOWED_PASSWORDS = config("DISALLOWED_PASSWORDS", cast=CommaSeparatedStrings)

REGISTRATION = config("REGISTRATION", cast=bool)
SESSION_PERMANENT = config("SESSION_PERMANENT", cast=bool)
DEBUG = config("DEBUG", cast=bool)

