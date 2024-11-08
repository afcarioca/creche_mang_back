FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=api.test"]