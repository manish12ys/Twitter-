# Use an official Python image as the base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy WSO2 configuration
COPY wso2.yaml /etc/wso2/wso2.yaml

# Expose the API port
EXPOSE 9443

# Start the Flask app
CMD ["python", "app.py"]

CMD gunicorn -w 4 -b 0.0.0.0:5000 app:app


