import anthropic
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, StreamingResponse

from .. import settings

app = FastAPI(title="A basic LLM-based app")

anthropic_client = anthropic.AsyncAnthropic(
    api_key=settings.anthropic_api_key,
)

# Choose a model from here: https://docs.anthropic.com/en/docs/about-claude/models
anthropic_model = "claude-3-haiku-20240307"


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
        model=anthropic_model,
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
        model=anthropic_model,
    )
    print(f"Usage: {message.usage}")
    out = message.content
    print(out)
    return PlainTextResponse(out[0].text)


# Response with streaming
async def _request_poem_about(theme: str):
    async with anthropic_client.messages.stream(
        max_tokens=1024,
        system="""You are a world-class poet. 
        You respond only with medium sized poems below 20 verses. 
        Also, you include only the poem, nothing more.""",
        messages=[
            {
                "role": "user",
                "content": f"Generate a poem about {theme}",
            }
        ],
        model=anthropic_model,
    ) as stream:
        async for text in stream.text_stream:
            yield text


@app.get("/streamed_poem_about", response_class=StreamingResponse)
async def streamed_poem_about(theme: str):
    """This endpoint generates a short poem about a theme

    :param theme: theme of the poem to generate
    :return: a plain text version of the poem
    """
    return StreamingResponse(_request_poem_about(theme))
