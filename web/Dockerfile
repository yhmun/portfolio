# Pull official base image
FROM python:3.8.3-slim-buster

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy web appliction files
COPY . /usr/src/app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run server
CMD gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000