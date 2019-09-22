FROM python:3.7

LABEL Name=ok-diet Version=1.0.0

WORKDIR /app
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system

COPY . .

CMD pipenv run web
