# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Set environment variable for Flask app
ENV FLASK_APP=run.py

# Run the app
CMD ["flask", "run", "--host", "0.0.0.0"]
