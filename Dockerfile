# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

FROM cypress/browsers:latest

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Heroku will dynamically assign
EXPOSE 5000

# Run the application using Gunicorn with dynamic port
CMD ["sh", "-c", "gunicorn -w 4 -b 0.0.0.0:${PORT:-5000} main:app"]
