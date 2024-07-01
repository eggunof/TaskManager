################################
# PYTHON-BASE
################################
FROM python:3.10.12-alpine as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    PROJECT_PATH="/app"

ENV PATH="$PROJECT_PATH/.venv/bin:$POETRY_HOME/bin:$PATH"


################################
# BUILDER-BASE
################################
FROM python-base as builder-base

RUN python3 -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION

WORKDIR $PROJECT_PATH
COPY poetry.lock pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache \
    poetry install --only main


################################
# DEVELOPMENT
################################
FROM python-base as development
WORKDIR $PROJECT_PATH

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PROJECT_PATH $PROJECT_PATH

RUN --mount=type=cache,target=/root/.cache \
    poetry install --with dev,lint

COPY taskmanager ./taskmanager

CMD ["uvicorn", "--factory", "taskmanager.presentation.api.main:create_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


################################
# PRODUCTION
################################
FROM python-base as production
WORKDIR $PROJECT_PATH

COPY --from=builder-base $PROJECT_PATH/.venv $PROJECT_PATH/.venv

COPY taskmanager ./taskmanager

CMD ["uvicorn", "--factory", "taskmanager.presentation.api.main:create_app", "--host", "0.0.0.0", "--port", "8000"]
