# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /dagster

# Install necessary libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Dagster project into the container
COPY . /dagster

# Expose the port Dagster will be accessible on
EXPOSE 3000 8888

# Set the default command to execute

# Copy the startup script into the container
COPY start.sh /dagster/start.sh

# Make the startup script executable
RUN chmod +x /dagster/start.sh

# Set the default command to execute the startup script
CMD ["/dagster/start.sh"]
