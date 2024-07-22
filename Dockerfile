FROM python:3.9-slim  # Use a lightweight Python base image

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt  # Install dependencies from requirements.txt

COPY . .

EXPOSE 5000  # Expose port 5000 for the Flask app

CMD ["python", "main.py"]  # Start the Flask app using `python main.py`
