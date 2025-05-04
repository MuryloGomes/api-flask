from . import api
from swagger.namespaces.alunoNamespace import alunos_ns
from swagger.namespaces.professorNamespace import professores_ns
from swagger.namespaces.turmaNamespace import turmas_ns

# Função para registrar os namespaces e configurar o Swagger
def configure_swagger(app):
    # Inicializa a API do Flask-RESTX com a aplicação Flask
    api.init_app(app)
    
    # Adiciona os namespaces à API com os respectivos caminhos
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professores_ns, path="/professores")
    api.add_namespace(turmas_ns, path="/turmas")
    
    # Desativa o Swagger UI na documentação (você pode habilitar ou personalizar se necessário)
    api.mask_swagger = False

    # Configurações adicionais do Swagger, como título e descrição
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'  # Expande a documentação automaticamente ao abrir
    app.config['SWAGGER_UI_ENABLED'] = True  # Habilita a interface do Swagger UI
    app.config['SWAGGER_UI_PATH'] = '/swagger'  # Define o caminho para acessar o Swagger UI
    
    # Caso queira adicionar uma descrição para a documentação da API
    app.config['SWAGGER_UI_TITLE'] = "API de Gestão de Alunos, Professores e Turmas"
    app.config['SWAGGER_UI_VERSION'] = "1.0"
