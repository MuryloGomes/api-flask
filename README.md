# API de Gestão de Alunos e Professores

Esta é uma API desenvolvida com Flask para gerenciar informações de alunos, professores e turmas. Ela oferece endpoints RESTful para realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em professores, alunos e turmas.

## Funcionalidades

### Gestão de Professores:
- Adicionar, atualizar, consultar e remover professores.

### Gestão de Alunos:
- Adicionar, atualizar, consultar e remover alunos.

### Gestão de Turmas:
- Adicionar, atualizar, consultar e remover turmas.

## Tecnologias Utilizadas

- **Flask**: Framework web para construir a API.
- **Python**: Linguagem de programação utilizada.
- **JSON**: Formato de troca de dados para a API.

## Instalação

### Requisitos

Certifique-se de ter o **Python 3.x** instalado em seu sistema.

### Passos para Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/MuryloGomes/api-flask.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd api-flask
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

    - **Para Linux/Mac**:
    
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    
    - **Para Windows**:
    
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute o servidor:

    ```bash
    python app.py
    ```

## Endpoints da API

### **Gestão de Professores**

#### 1. **GET /professores**
Obtém a lista de todos os professores.

- **Resposta**:

    - **Status 200**: Retorna a lista de professores.

    **Exemplo**:
    
    ```json
    [
      {
        "id": "1",
        "nome": "Carlos Silva",
        "idade": 40,
        "materia": "Matemática",
        "observacoes": "Bom professor"
      }
    ]
    ```

#### 2. **POST /professores**
Cria um novo professor.

- **Corpo da Requisição (JSON)**:

    ```json
    {
      "nome": "Carlos Silva",
      "idade": 40,
      "materia": "Matemática",
      "observacoes": "Bom professor"
    }
    ```

- **Resposta**:

    - **Status 201**: Professor criado com sucesso.

    **Exemplo**:
    
    ```json
    {
      "id": "ab9ec299-1621-4496-8426-521543cc8c4a",
      "nome": "Carlos Silva",
      "idade": 40,
      "materia": "Matemática",
      "observacoes": "Bom professor"
    }
    ```

#### 3. **GET /professores/<string:id>**
Obtém as informações de um professor específico pelo ID.

- **Parâmetros**:
    - `id`: ID do professor.

- **Resposta**:

    - **Status 200**: Retorna os dados do professor.
    - **Status 404**: Professor não encontrado.

    **Exemplo**:
    
    ```json
    {
      "id": "ab9ec299-1621-4496-8426-521543cc8c4a",
      "nome": "Carlos Silva",
      "idade": 40,
      "materia": "Matemática",
      "observacoes": "Bom professor"
    }
    ```

#### 4. **PUT /professores/<string:id>**
Atualiza as informações de um professor existente pelo ID.

- **Parâmetros**:
    - `id`: ID do professor.

- **Corpo da Requisição (JSON)**:

    ```json
    {
      "nome": "Carlos Silva",
      "idade": 41,
      "materia": "Física",
      "observacoes": "Excelente professor"
    }
    ```

- **Resposta**:

    - **Status 200**: Professor atualizado com sucesso.

    **Exemplo**:
    
    ```json
    {
      "id": "ab9ec299-1621-4496-8426-521543cc8c4a",
      "nome": "Carlos Silva",
      "idade": 41,
      "materia": "Física",
      "observacoes": "Excelente professor"
    }
    ```

#### 5. **DELETE /professores/<string:id>**
Remove um professor pelo ID.

- **Parâmetros**:
    - `id`: ID do professor.

- **Resposta**:

    - **Status 200**: Professor removido com sucesso.

    **Exemplo**:
    
    ```json
    {
      "message": "Professor com id ab9ec299-1621-4496-8426-521543cc8c4a foi removido com sucesso."
    }
    ```


## Endpoints da API

### **Gestão de Professores**

#### 1. **GET /professores**
Obtém a lista de todos os professores.

- **Resposta**:

    - **Status 200**: Retorna a lista de professores.

    **Exemplo**:
    
    ```json
    [
      {
        "id": "1",
        "nome": "Carlos Silva",
        "idade": 40,
        "materia": "Matemática",
        "observacoes": "Bom professor"
      }
    ]
    ```

#### 2. **POST /professores**
Cria um novo professor.

- **Corpo da Requisição (JSON)**:

    ```json
    {
      "nome": "Carlos Silva",
      "idade": 40,
      "materia": "Matemática",
      "observacoes": "Bom professor"
    }
    ```

- **Resposta**:

    - **Status 201**: Professor criado com sucesso.

    **Exemplo**:
    
    ```json
    {
      "id": "ab9ec299-1621-4496-8426-521543cc8c4a",
      "nome": "Carlos Silva",
      "idade": 40,
      "materia": "Matemática",
      "observacoes": "Bom professor"
    }
    ```

#### 3. **GET /professores/<string:id>**
Obtém as informações de um professor específico pelo ID.

- **Parâmetros**:
    - `id`: ID do professor.

- **Resposta**:

    - **Status 200**: Retorna os dados do professor.
    - **Status 404**: Professor não encontrado.

    **Exemplo**:
    
    ```json
    {
      "id": "ab9ec299-1621-4496-8426-521543cc8c4a",
      "nome": "Carlos Silva",
      "idade": 40,
      "materia": "Matemática",
      "observacoes": "Bom professor"
    }
    ```

#### 4. **PUT /professores/<string:id>**
Atualiza as informações de um professor existente pelo ID.

- **Parâmetros**:
    - `id`: ID do professor.

- **Corpo da Requisição (JSON)**:

    ```json
    {
      "nome": "Carlos Silva",
      "idade": 41,
      "materia": "Física",
      "observacoes": "Excelente professor"
    }
    ```

- **Resposta**:

    - **Status 200**: Professor atualizado com sucesso.

    **Exemplo**:
    
    ```json
    {
      "id": "ab9ec299-1621-4496-8426-521543cc8c4a",
      "nome": "Carlos Silva",
      "idade": 41,
      "materia": "Física",
      "observacoes": "Excelente professor"
    }
    ```

#### 5. **DELETE /professores/<string:id>**
Remove um professor pelo ID.

- **Parâmetros**:
    - `id`: ID do professor.

- **Resposta**:

    - **Status 200**: Professor removido com sucesso.

    **Exemplo**:
    
    ```json
    {
      "message": "Professor com id ab9ec299-1621-4496-8426-521543cc8c4a foi removido com sucesso."
    }
    ```