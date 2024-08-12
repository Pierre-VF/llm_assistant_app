"""
Module containing the main app
"""

from fastapi import FastAPI

try:
    from src import settings
except ImportError:
    from .src import settings

app = FastAPI()

# Just imported for now (will actually be used later)
s = settings

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
