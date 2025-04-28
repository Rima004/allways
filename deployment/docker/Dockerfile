FROM python:3.11

WORKDIR /usr/app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry && poetry install

COPY . .

ENV DJANGO_SETTINGS_MODULE='config.settings'

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8001"]
