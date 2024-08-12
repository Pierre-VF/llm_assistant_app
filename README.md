# llm_assistant_app
A toy example of an LLM assistant app


## Installation

Run:
> pipx install poetry

Ensure that Python 3.12 is used (if your machine does not point to it by default)
> poetry use python3.12

Install the dependencies with development mode:
> poetry install --all-extras

Then create your **.env** file:
```
ANTHROPIC_API_KEY='ThisIsYourAPIkey'
DEBUG=False
```

## Running the app

Just run:
> python llm_assistant_app/app.py