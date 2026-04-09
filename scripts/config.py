import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

BLS_API_KEY = os.getenv("BLS_API_KEY")
FRED_API_KEY = os.getenv("FRED_API_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")