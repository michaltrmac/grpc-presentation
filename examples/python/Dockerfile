FROM eu.gcr.io/collaborativemanagement-212609/python/grpc:1.19.0-alpine

COPY requirements.txt requirements.txt

RUN apk add --no-cache postgresql-libs && \
            apk add --no-cache --virtual .build-deps gcc git musl-dev openssh-client postgresql-dev && \
            python -m pip install -r requirements.txt --no-cache-dir && \
            apk --purge del .build-deps

CMD ["python", "server.py"]
