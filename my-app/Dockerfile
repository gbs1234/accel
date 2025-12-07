# Use an official lightweight Python image
FROM python:3.13-slim

# Create and set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port Cloud Run expects (8080)
EXPOSE 8080

# Use Gunicorn to serve the app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]