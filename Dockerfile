# Use official Python image as the base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8000

# Command to run Streamlit when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
