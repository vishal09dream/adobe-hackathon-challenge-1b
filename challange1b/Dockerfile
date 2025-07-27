
FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the updated main script (contains the modified code)
COPY main.py .

# Copy the Challenge_1b directory with all subdirectories and files
COPY Challenge_1b/ ./Challenge_1b/

# Set Python path to avoid any import issues
ENV PYTHONPATH=/app

# Run the application
CMD ["python", "main.py"]
