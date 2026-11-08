import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]
THRESHOLD=0.5
# DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/mydb"
