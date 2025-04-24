FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  build-essential \
  curl \
  wget \
  git \
  vim \
  nano \
  htop \
  postgresql \
  postgresql-contrib \
  nginx \
  nodejs \
  npm \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY . .

RUN uv sync --locked

EXPOSE 8000

ENV DEBUG=True \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  NODE_ENV=development \
  FLASK_ENV=development

CMD ["uv", "run", "main.py"]
