"""
Module containing a UI with FastHTML
"""

from fasthtml.common import (
    H2,
    Body,
    Button,
    FastHTML,
    P,
    RedirectResponse,
    Style,
    picolink,
)

css = Style(":root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}")
body_css = Style("body {margin: 40px;}")
app = FastHTML(hdrs=(picolink, css, body_css))


@app.get("/")
def home():
    return RedirectResponse("joker")


@app.get("/joker")
def joker():
    return Body(
        H2("Joke of the day"),
        P("(...)", id="daily_joke_p"),
        Button(
            "Generate",
            hx_get="../api/nerdy_joker",
            hx_target="#daily_joke_p",
            hx_swap="innerHTML",
        ),
    )
