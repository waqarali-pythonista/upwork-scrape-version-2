# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    --no-install-recommends

# Add Google Chrome's official GPG key
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-keyring.gpg

# Add Google Chrome's repository to apt sources
RUN echo "deb [signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Python is available (install if needed)
RUN apt-get update && apt-get install -y python3 python3-pip
# Expose the port that Heroku will dynamically assign
EXPOSE 5000

# Run the application using Gunicorn with dynamic port
CMD ["sh", "-c", "gunicorn -w 4 -b 0.0.0.0:${PORT:-5000} main:app"]
