FROM python:3.7-alpine

COPY main.py .

CMD ["python3", "main.py"]