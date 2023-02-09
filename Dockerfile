# Lighter version of python
FROM python:3.1-slim-buster

WORKDIR /app

# Copy requirements.txt from computer to image with the same filename
COPY requirements.txt requirements.txt

# Install requirements specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy all files from directory where requirements.txt is located.
COPY . .

# Run command line to start the server @ port 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]