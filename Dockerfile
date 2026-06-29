# API DescomplicaBusiness - Trabalho Final Cloud Computing
FROM python:3.12-slim

WORKDIR /app

# Instala dependências primeiro (aproveita cache de camada do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da API
COPY api/ ./api/

EXPOSE 5000

# Sobe a API (host 0.0.0.0 para ficar acessível fora do container)
CMD ["python", "api/app.py"]
