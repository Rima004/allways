FROM python:3.11

WORKDIR /usr/app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry && poetry install

COPY apps .
COPY config .
COPY static .
COPY templates .
COPY manage.py .
COPY db.sqlite3 .

CMD ["python", "manage.py", "runserver", "8001"]