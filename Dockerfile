# Usa uma imagem oficial do Python leve
FROM python:3.10-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências primeiro (otimiza o build)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Comando que executa o script ao iniciar o container
CMD ["python", "main.py"]
