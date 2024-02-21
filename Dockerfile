# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make sure to expose the port the app runs on
EXPOSE 23

# Run the script when the container launches
CMD ["python", "as400honey.py"]
