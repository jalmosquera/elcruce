FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv sync --frozen --no-install-project

COPY . .

RUN uv sync --frozen

CMD ["uv", "run", "uvicorn", "src.core.main:app", "--host", "0.0.0.0", "--port", "8000"]
