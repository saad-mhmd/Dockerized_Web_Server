# Specifies the base image as Python 3.8 from which to build this Docker image
FROM python:3.8

# Sets the working directory inside the Docker container to /app. All subsequent commands will be executed relative to this directory.
WORKDIR /app

# Copies the requirements.txt file from the local directory to the /app directory in the Docker image.
COPY requirements.txt .

# Executes the command to install Python dependencies listed in requirements.txt using pip.
# The --no-cache-dir flag prevents caching of downloaded packages, ensuring a clean installation.
RUN pip install --no-cache-dir -r requirements.txt

# Copies the entire local directory (including all files and folders) to the /app directory in the Docker image.
COPY . .

# Installs the Flask-SQLAlchemy library inside the Docker image.
# This library is necessary for integrating SQLAlchemy with Flask for database interactions.
RUN pip install Flask-SQLAlchemy

# Copies the templates directory from the local directory to the /app/templates directory within the Docker image.
# This likely includes HTML templates used by the Flask application for rendering views.
COPY templates /app/templates

# Defines the command to run when the container starts.
# Starts the Flask application (app.py) by executing python app.py within the /app directory in the container.
CMD ["python", "app.py"]