FROM python:3.7-alpine

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy all relevant lib
COPY main.py .
COPY lib lib

# Copy unittests and run them
COPY test test
RUN python3 -m unittest discover

CMD ["python3", "main.py"]