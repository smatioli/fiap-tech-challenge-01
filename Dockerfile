# Use Python 3.11 slim image as base
FROM python:3.11-slim as builder

# Install poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy dependency files
COPY production-app/pyproject.toml production-app/poetry.lock ./

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy application code
COPY production-app/ .

# Create a new stage for the runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Expose the port the app runs on
EXPOSE ${PORT}

# Command to run the application
CMD ["python", "-m", "production-app"] 