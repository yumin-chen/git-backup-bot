# Stage 1: Builder
FROM python:3.11-alpine AS builder

WORKDIR /usr/src/app

# Install build dependencies
RUN pip install --upgrade pip

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Stage 2: Final Image
FROM python:3.11-alpine

WORKDIR /usr/src/app

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Create and set permissions for the logs directory
RUN mkdir -p /usr/src/app/logs && chown appuser:appgroup /usr/src/app/logs

USER appuser

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/src/app .

# Expose the metrics port
EXPOSE 9090

# Set the entrypoint for the container
ENTRYPOINT ["python", "src/main.py"]
