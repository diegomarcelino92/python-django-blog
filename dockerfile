FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV IMG_USER "dbuser"
ENV PATH="/scripts:/venv/bin:$PATH"

COPY ./apps /apps
COPY ./project /project
COPY ./scripts /scripts
COPY ./requirements.txt /requirements.txt
COPY ./manage.py /manage.py

WORKDIR /

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r ../requirements.txt && \
    adduser --disabled-password --no-create-home $IMG_USER && \
    mkdir -p /data/static && \
    mkdir -p /data/media && \
    chown -R $IMG_USER:$IMG_USER /venv && \
    chown -R $IMG_USER:$IMG_USER /data/static && \
    chown -R $IMG_USER:$IMG_USER /data/media && \
    chmod -R 755 /data/static && \
    chmod -R 755 /data/media && \
    chmod -R +x /scripts


USER $IMG_USER
EXPOSE 8000
CMD ["docker-entrypoint.sh"]

