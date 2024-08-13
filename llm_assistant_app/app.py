"""
Module containing the main app


Notes:
- The doc of the Anthropic API is available here: https://github.com/anthropics/anthropic-sdk-python

"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# To support different relative import syntax between tools and calls
try:
    from src import api, ui  # type: ignore
except ImportError:
    from .src import api, ui

app = FastAPI(title="A basic LLM-based app")


# Mounting sub-apps
app.mount("/ui", ui.app)
app.mount("/api", api.app)


# Redirecting base to the UI
@app.get("/")
async def home():
    return RedirectResponse("/ui/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8080)
