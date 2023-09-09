# Use uma imagem base apropriada para a sua aplicação (por exemplo, python:3.11)
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt do contexto de build para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o código-fonte da aplicação para o contêiner
COPY /src /app

# Comando para iniciar o seu bot (ajuste conforme necessário)
CMD ["python", "main.py"]
