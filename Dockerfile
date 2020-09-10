FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY api/ /app/api
COPY app.py /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]