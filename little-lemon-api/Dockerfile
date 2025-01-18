FROM python:3.10
LABEL maintainer="Ahmed Shehab <a.shehab.biomedeng@gmail.com>"

WORKDIR /little-lemon-api

COPY Pipfile  /little-lemon-api/
RUN pip install --upgrade pip \
	&& pip install pipenv
	
RUN pipenv install --skip-lock --system

COPY . /little-lemon-api


# VOLUME /little-lemon-api/db.sqlite3
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

