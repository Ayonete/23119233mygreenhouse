FROM python:3.12.2

# ENV PYTHONBUFFERED=1

# ENV PORT=8080

WORKDIR ./

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
# RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


