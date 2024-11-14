FROM python:3.12.2

# ENV PYTHONBUFFERED=1

# ENV PORT=8080

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
# RUN python manage.py migrate

EXPOSE 8000

CMD gunicorn mygreenhouse.wsgi:application --bind 0.0.0.0:"${PORT}"

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


