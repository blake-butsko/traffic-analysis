# Start from a Python base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any dependencies
RUN pip install pandas

# Run the Python code
CMD ["python", "traffic-analysis.py"]
