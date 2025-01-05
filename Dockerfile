FROM python:3.10
LABEL maintainer="Ahmed Shehab <a.shehab.biomedeng@gmail.com>"

WORKDIR /littlelemon_booking

COPY Pipfile  .
RUN pip install --upgrade pip \
        && pip install pipenv

RUN pipenv install --skip-lock --system

COPY . .

VOLUME /littlelemon_booking/db

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
