FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app ./app

EXPOSE 8000
CMD ["python", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]