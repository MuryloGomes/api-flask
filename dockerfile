# Usando uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requisitos para o container
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para dentro do container
COPY . .

# Expor a porta que o Flask irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
