# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory (optional)
WORKDIR /app

# Install Apache and any necessary dependencies
RUN apt-get update && apt-get install -y \
    apache2 \
    && rm -rf /var/lib/apt/lists/*

# Expose the default Apache port (optional if you want to access Apache)
EXPOSE 80

# Start Apache in the background and then sleep
CMD ["/bin/sh", "-c", "apache2ctl start && sleep 8999"]
