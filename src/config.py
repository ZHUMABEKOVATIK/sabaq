# dotenv
from dotenv import load_dotenv
load_dotenv()
import os

DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")

DB_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"
DB_URL_2 = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"