"""
Module containing the main app


Notes:
- The doc of the Anthropic API is available here: https://github.com/anthropics/anthropic-sdk-python

"""

import anthropic
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, RedirectResponse

# To support different relative import syntax between tools and calls
try:
    from src import settings  # type: ignore
except ImportError:
    from .src import settings

app = FastAPI(title="A basic LLM-based app")

anthropic_client = anthropic.AsyncAnthropic(
    api_key=settings.anthropic_api_key,
)


# Redirecting base to docs
@app.get("/")
async def home():
    return RedirectResponse("/docs")


@app.get("/short_poem_about", response_class=PlainTextResponse)
async def poem_about(theme: str):
    """This endpoint generates a short poem about a theme

    :param theme: theme of the poem to generate
    :return: a plain text version of the poem
    """
    message = await anthropic_client.messages.create(
        max_tokens=1024,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": f"Generate a poem about {theme}",
            }
        ],
        model="claude-3-5-sonnet-20240620",
    )
    print(f"Usage: {message.usage}")
    out = message.content
    print(out)
    return PlainTextResponse(out[0].text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8080)
