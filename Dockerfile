# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first, to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install the required Python dependencies
RUN python -m pip install -r requirements.txt

# Now copy the rest of the application files
COPY . /app

# Expose port 8000 to allow connections
EXPOSE 8000

# Run the Django development server on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
