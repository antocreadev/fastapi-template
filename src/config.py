import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_PORT = os.getenv("A")
POSTGRES_DB = os.getenv("POSTGRES_DB")

TITLE = "Template API FastAPI"
DESCRIPTION = "This is the API documentation for the Template API FastAPI"
TAGS_METADATA = [
     {
        "name": "Server",
        "description": "Monitor the server state",
    },
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {
        "name": "Auth",
        "description": "Operations with Auth.",
    },
]
