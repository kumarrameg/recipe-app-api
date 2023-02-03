FROM python:3.9-alpine.13
LABEL maintainer="Kumarrameg"

ENV PYTHONBUFFERED 1

COPY ./requirments.txt /tmp/requirments.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
  /py/bin/pip install && \
  —upgrade pip && \
  /py/bin/pip install —r /tmp/requirements. txt && \
  rm —rf /tmp && \
  adduser \
    —disabled—password \
    ——no—c reate-home \
    django—user
ENV PATH="/py/bin:$PATH"
USER django-user