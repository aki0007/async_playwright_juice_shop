# Use an official Python image as the base
FROM python:3.11-slim

# Set working directory to /app
WORKDIR /app

# Copy project files
COPY . .

# Install Docker
RUN apt-get update && apt-get install -y docker.io

# Install Docker CLI
RUN apt-get install -y docker-compose

# Install dependencies
RUN pip install -r requirements/common.in

# Install Playwright and its browsers
RUN pip install playwright
RUN playwright install

# Set environment variables
ENV ENVIRONMENT=development
ENV LOCAL=1

# Run command to start tests when container starts
CMD ["pytest", "tests/"]
