FROM python:3.13-slim

WORKDIR /app

COPY main.py .
COPY modelos.py .
COPY inventario.py .
COPY ativos.json .

CMD ["python", "main.py"]