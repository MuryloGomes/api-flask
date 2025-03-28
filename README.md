API de Gestão de Alunos e Professores
Esta é uma API desenvolvida com Flask para gerenciar informações de alunos, professores e turmas. Ela oferece endpoints RESTful para realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em professores, alunos e turmas.

Funcionalidades
Gestão de Professores: Adicionar, atualizar, consultar e remover professores.

Gestão de Alunos: Adicionar, atualizar, consultar e remover alunos.

Gestão de Turmas: Adicionar, atualizar, consultar e remover turmas.

Tecnologias Utilizadas
Flask: Framework web para construir a API.

Python: Linguagem de programação utilizada.

JSON: Formato de troca de dados para a API.

Instalação
Requisitos
Certifique-se de ter o Python 3.x instalado em seu sistema.

Passos para Instalação
Clone o repositório:

bash
Copiar
git clone https://seu-repositorio.git
Navegue até o diretório do projeto:

bash
Copiar
cd nome-do-projeto
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
Instale as dependências:

bash
Copiar
pip install -r requirements.txt
Execute o servidor:

bash
Copiar
python app.py
O servidor estará disponível em http://127.0.0.1:5000/ por padrão.

Endpoints da API
1. GET /professores
Obtém a lista de todos os professores.

Resposta:

Status 200: Retorna a lista de professores.

Exemplo:

json
Copiar
[
  {
    "id": 1,
    "nome": "Carlos Silva",
    "idade": 40,
    "disciplina": "Matemática",
    "observacoes": "Bom professor"
  }
]
2. GET /professores/int:id
Obtém as informações de um professor específico pelo ID.

Parâmetros:

id: ID do professor.

Resposta:

Status 200: Retorna os dados do professor.

Status 404: Professor não encontrado.

Exemplo:

json
Copiar
{
  "id": 1,
  "nome": "Carlos Silva",
  "idade": 40,
  "disciplina": "Matemática",
  "observacoes": "Bom professor"
}
3. POST /professores
Cria um novo professor.

Corpo da Requisição (JSON):

json
Copiar
{
  "nome": "Carlos Silva",
  "idade": 40,
  "disciplina": "Matemática",
  "observacoes": "Bom professor"
}
Resposta:

Status 201: Professor criado com sucesso.

Exemplo:

json
Copiar
{
  "id": 1,
  "nome": "Carlos Silva",
  "idade": 40,
  "disciplina": "Matemática",
  "observacoes": "Bom professor"
}
4. PUT /professores/int:id
Atualiza as informações de um professor existente pelo ID.

Parâmetros:

id: ID do professor.

Corpo da Requisição (JSON):

json
Copiar
{
  "nome": "Carlos Silva",
  "idade": 41,
  "disciplina": "Física",
  "observacoes": "Excelente professor"
}
Resposta:

Status 200: Professor atualizado com sucesso.

Exemplo:

json
Copiar
{
  "id": 1,
  "nome": "Carlos Silva",
  "idade": 41,
  "disciplina": "Física",
  "observacoes": "Excelente professor"
}
5. DELETE /professores/int:id
Remove um professor pelo ID.

Parâmetros:

id: ID do professor.

Resposta:

Status 200: Professor removido com sucesso.

Exemplo:

json
Copiar
{
  "message": "Professor com id 1 foi removido com sucesso."
}
6. GET /alunos
Obtém a lista de todos os alunos.

Resposta:

Status 200: Retorna a lista de alunos.

Exemplo:

json
Copiar
[
  {
    "id": 1,
    "nome": "Carlos Silva",
    "idade": 20,
    "turma": "Matemática",
    "data_nasc": "2003-05-20",
    "nota_primeiro_sem": 8.5,
    "nota_segundo_sem": 9.0
  }
]
(Continue com os outros endpoints de Alunos e Turmas da mesma forma.)

Como Contribuir
Faça um fork deste repositório.

Crie uma branch para a sua feature (git checkout -b feature/nome-da-feature).

Faça as alterações e comite (git commit -am 'Adiciona nova feature').

Envie a sua branch para o repositório remoto (git push origin feature/nome-da-feature).

Abra um pull request.