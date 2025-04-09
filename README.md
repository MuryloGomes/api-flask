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


