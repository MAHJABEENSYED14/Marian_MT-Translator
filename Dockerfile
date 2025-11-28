FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy the requirements file first (for caching layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app into the container
COPY . .

# Expose port 5005 so Docker knows it’s for external access
EXPOSE 5006

# Set environment variable so Flask knows which file to run
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5006

# Run the app
CMD ["flask", "run"]
