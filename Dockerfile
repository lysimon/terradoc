FROM python:3.7-alpine

# Copy all relevant configuration
COPY main.py .
COPY configuration configuration
COPY storage storage

# Copy unittests and run them
COPY test test
RUN python3 -m unittest discover

CMD ["python3", "main.py"]