# Use the Alpine Linux base image
FROM alpine:latest

# Install curl package
RUN apk add --no-cache curl

# Copy the config.txt file to the /app directory in the container
COPY config.txt /app/config.txt

# Default command to keep the container running (can be overridden)
CMD ["tail", "-f", "/dev/null"]
