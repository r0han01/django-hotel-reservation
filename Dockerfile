# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies (optional, e.g., for handling static files or building certain dependencies)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Django will run on (default is 8000)
EXPOSE 8000

# The command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
