FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --update add --no-cache \
    git gcc build-base zlib-dev jpeg-dev curl

COPY . /fapesp_app
WORKDIR /fapesp_app

RUN pip --no-cache-dir install -r requirements.txt

RUN chown -R nobody:nogroup /fapesp_app
USER nobody
EXPOSE 8000

CMD gunicorn --workers 3 --bind 0.0.0.0:8000 app:app --timeout 150 --log-level DEBUG