import os
from dotenv import load_dotenv

load_dotenv(".env")

env_vars = {
    "port": os.getenv("PORT")
}