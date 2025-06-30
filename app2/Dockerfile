# FROM python:3.8

# EXPOSE 8081
# WORKDIR /app2

# COPY . ./

# RUN pip install -r requirements.txt

# CMD ["python", "app.py"]

#########################
## Second app Dockerfile
# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install pip and setuptools (good practice, though sometimes already present)
RUN pip install --no-cache-dir pip setuptools

# Copy the requirements file into the container at /app
# We create a requirements.txt with pyfiglet inside it.
# Content of requirements.txt:
# pyfiglet==1.0.0
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY app.py .

# Define environment variable (optional, but good for indicating app purpose)
ENV NAME "Funky ASCII Art App"

# Run the Python application when the container starts
CMD ["python", "app.py"]

