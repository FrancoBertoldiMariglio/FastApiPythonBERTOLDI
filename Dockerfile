# Use an official Python runtime as a parent image
FROM python:3.11.6-slim-bullseye AS builder

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

# Start a new stage to create a smaller image
FROM python:3.11.6-slim-bullseye

# Copy installed packages from previous stage
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Run main.py when the container launches
CMD ["python", "-m", "main"]