FROM python:3.10-alpine3.15
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update
RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
ENTRYPOINT [ "/app/entrypoint.sh" ]