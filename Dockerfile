FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV USER=app
ENV APP_HOME=/home/app/TestNews


RUN pip install --upgrade pip

# install psycopg2 dependencies
RUN apk update && apk add libpq
RUN apk add postgresql-dev gcc python3-dev musl-dev

# install Pillow

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev libjpeg-turbo \
    && apk del build-deps \
    && apk add jpeg-dev zlib-dev libjpeg libjpeg-turbo \
    && pip install Pillow
COPY req.txt .

RUN pip install -r req.txt

ADD . $APP_HOME

WORKDIR $APP_HOME

ENTRYPOINT ["/home/app/TestNews/entrypoint.prod.sh"]