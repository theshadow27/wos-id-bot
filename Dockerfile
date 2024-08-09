# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*.py .

# Make port 80 available to the world outside this container (optional if needed)
EXPOSE 80

# Run bot.py when the container launches
CMD ["python", "./cli.py"]
