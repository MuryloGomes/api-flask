from flask_restx import Api

# Criação do objeto da API do Flask-RESTX
api = Api(
    title="API Escolar",
    version="1.0",
    description="Documentação Swagger da API de alunos, professores e turmas",
    doc="/docs",
    mask_swagger=False,  # Desativa o X-Fields no Swagger,
    prefix="/api"
)