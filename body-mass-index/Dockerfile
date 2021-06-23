FROM python:3.9

ENV APP_HOME /body-mass-index
WORKDIR $ APP_HOME
COPY . ./

RUN pip install Flask gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
