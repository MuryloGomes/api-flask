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

### **Gestão de Alunos**

#### 1. **GET /alunos**
Obtém a lista de todos os alunos.

- **Resposta**:

    - **Status 200**: Retorna a lista de alunos.

    **Exemplo**:
    
    ```json
    [
      {
        "aluno_id": "cd9e9015-6546-40c9-8d8d-6d94aa895c36",
        "data_nascimento": "2003-05-20",
        "idade": 20,
        "media_final": 8.75,
        "nome": "Carlos Silva",
        "nota_primeiro_semestre": 8.5,
        "nota_segundo_semestre": 9.0,
        "turma_id": "23fbc062-b857-4c31-af67-fc50b9012064"
      }
    ]
    ```

#### 2. **POST /alunos**
Cria um novo aluno.

- **Corpo da Requisição (JSON)**:

    ```json
    {
      "nome": "Carlos Silva",
      "idade": 20,
      "turma": "23fbc062-b857-4c31-af67-fc50b9012064",
      "data_nasc": "2003-05-20",
      "nota_primeiro_sem": 8.5,
      "nota_segundo_sem": 9.0
    }
    ```

- **Resposta**:

    - **Status 201**: Aluno criado com sucesso.

    **Exemplo**:
    
    ```json
    {
      "aluno_id": "cd9e9015-6546-40c9-8d8d-6d94aa895c36",
      "data_nascimento": "2003-05-20",
      "idade": 20,
      "media_final": 8.75,
      "nome": "Carlos Silva",
      "nota_primeiro_semestre": 8.5,
      "nota_segundo_semestre": 9.0,
      "turma_id": "23fbc062-b857-4c31-af67-fc50b9012064"
    }
    ```

#### 3. **GET /alunos/<string:id>**
Obtém as informações de um aluno específico pelo ID.

- **Parâmetros**:
    - `id`: ID do aluno.

- **Resposta**:

    - **Status 200**: Retorna os dados do aluno.
    - **Status 404**: Aluno não encontrado.

    **Exemplo**:
    
    ```json
    {
      "aluno_id": "cd9e9015-6546-40c9-8d8d-6d94aa895c36",
      "data_nascimento": "2003-05-20",
      "idade": 20,
      "media_final": 8.75,
      "nome": "Carlos Silva",
      "nota_primeiro_semestre": 8.5,
      "nota_segundo_semestre": 9.0,
      "turma_id": "23fbc062-b857-4c31-af67-fc50b9012064"
    }
    ```

#### 4. **PUT /alunos/<string:id>**
Atualiza as informações de um aluno existente pelo ID.

- **Parâmetros**:
    - `id`: ID do aluno.

- **Corpo da Requisição (JSON)**:

    ```json
    {
      "nome": "Carlos Teste",
      "turma": "23fbc062-b857-4c31-af67-fc50b9012064",
      "data_nasc": "2003-05-20",
      "nota_primeiro_sem": 8.7,
      "nota_segundo_sem": 9.2
    }
    ```

- **Resposta**:

    - **Status 200**: Aluno atualizado com sucesso.

    **Exemplo**:
    
    ```json
    {
      "aluno_id": "cd9e9015-6546-40c9-8d8d-6d94aa895c36",
      "data_nascimento": "2003-05-20",
      "idade": 20,
      "media_final": 8.75,
      "nome": "Carlos Teste",
      "nota_primeiro_semestre": 8.5,
      "nota_segundo_semestre": 9.0,
      "turma_id": "23fbc062-b857-4c31-af67-fc50b9012064"
    }
    ```

#### 5. **DELETE /alunos/<string:id>**
Remove um aluno pelo ID.

- **Parâmetros**:
    - `id`: ID do aluno.

- **Resposta**:

    - **Status 200**: Aluno removido com sucesso.

    **Exemplo**:
    
    ```json
    {
      "message": "Aluno com id cd9e9015-6546-40c9-8d8d-6d94aa895c36 foi removido com sucesso."
    }
    ```

## Como Contribuir

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para a sua feature (ex: `git checkout -b feature/nome-da-feature`).
3. Faça as alterações e **comite** (ex: `git commit -am

 'Adicionando nova feature'`).
4. **Push** para sua branch (ex: `git push origin feature/nome-da-feature`).
5. Abra um **pull request**.
