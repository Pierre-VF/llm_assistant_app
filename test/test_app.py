from fastapi.testclient import TestClient

from llm_assistant_app.app import app


def test_app():
    c = TestClient(app)

    # Making sure that the app starts as intended
    assert c.get("/").status_code in [200, 307]

    # Making sure that the Anthropic API call works
    poem_response = c.get("/api/short_poem_about?theme=the sea")
    assert poem_response.status_code == 200
    assert isinstance(poem_response.text, str)
    assert len(poem_response.text) > 10
