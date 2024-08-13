import anthropic
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from .. import settings

app = FastAPI(title="A basic LLM-based app")

anthropic_client = anthropic.AsyncAnthropic(
    api_key=settings.anthropic_api_key,
)


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


@app.get("/nerdy_joker", response_class=PlainTextResponse)
async def nerdy_joker():
    """This endpoint generates a nerdy joke

    :return: a plain text version of the joke
    """
    message = await anthropic_client.messages.create(
        max_tokens=1024,
        system="You are a world-class joker and nerd. Respond only with short jokes.",
        messages=[
            {
                "role": "user",
                "content": "Tell me a joke",
            }
        ],
        model="claude-3-5-sonnet-20240620",
    )
    print(f"Usage: {message.usage}")
    out = message.content
    print(out)
    return PlainTextResponse(out[0].text)
