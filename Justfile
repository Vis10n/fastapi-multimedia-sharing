# Load .env file automatically
set dotenv-load := true
set positional-arguments := true

PYTHON_VERSION := "3.13"

# Run server
run-server:
    uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000;
