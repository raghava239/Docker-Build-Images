# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory (optional)
WORKDIR /app

# Install any necessary dependencies (optional)
RUN apt-get update && apt-get install -y \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Command to execute when the container starts
CMD ["/bin/sh", "-c", "sleep 8999"]
