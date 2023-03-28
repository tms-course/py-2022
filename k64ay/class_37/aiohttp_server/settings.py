import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

PORT = 7000

DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite+aiosqlite:///sqlite.db')
