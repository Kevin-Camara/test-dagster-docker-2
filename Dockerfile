FROM python:3.11-slim

RUN pip install dagster

WORKDIR /app
COPY . /app

# Expõe porta para gRPC
EXPOSE 4266

# Inicia APENAS o servidor gRPC
CMD ["dagster", "api", "grpc", "--python-file", "definitions.py", "--host", "0.0.0.0", "--port", "4266"]
