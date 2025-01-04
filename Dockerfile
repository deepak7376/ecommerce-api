# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 8000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_CONFIG=config.ProductionConfig

# Set the entrypoint to start the app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
