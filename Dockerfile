#alpine: light weight version of python
FROM python:3.7-alpine
MAINTAINER Abdlrahman

# run python in unbuffered mode, it's recommend when run python by docker, avoid some complication
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create user to run our application
RUN adduser -D user

# switch docker to the user that we created it, create sperate user for our app it's more secure
USER user