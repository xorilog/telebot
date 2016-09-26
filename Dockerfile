FROM alpine
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
COPY app /app
WORKDIR /app
RUN pip install twx.botapi
