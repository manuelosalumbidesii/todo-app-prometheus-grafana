# Dockerfile

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code
COPY ./app /app/app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
