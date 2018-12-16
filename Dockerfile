FROM python:3.7-alpine

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy all relevant classes
COPY main.py .
COPY classes classes

# Copy unittests and run them
COPY test test
RUN python3 -m unittest discover

CMD ["python3", "main.py"]