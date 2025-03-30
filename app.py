import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'model'))

from flask import Flask, jsonify, request
from datetime import datetime
from model.professorModel import Professor, professores, add_professor
from model.alunoModel import Aluno, get_alunos, get_aluno_by_id, remove_aluno  
from model.turmaModel import Turma, get_turmas, get_turma_by_id, remove_turma  
app = Flask(__name__)

@app.route('/')
def hello():
    return "Seja Bem-vindo!"

# CRUD PROFESSORES

@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify([professor.to_dict() for professor in professores]), 200

@app.route('/professores', methods=['POST'])
def add_professor_route():
    data = request.get_json()

    required_fields = ['nome', 'idade', 'materia', 'observacoes']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400

    professor = add_professor(data)
    return jsonify(professor.to_dict()), 201

@app.route('/professores/<string:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if professor is None:
        return jsonify({"error": "Professor não encontrado"}), 404
    return jsonify(professor.to_dict()), 200

@app.route('/professores/<string:id>', methods=['PUT'])
def update_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if professor is None:
        return jsonify({"error": "Professor não encontrado"}), 404

    data = request.get_json()

    if 'nome' in data:
        professor.nome = data['nome']
    if 'idade' in data:
        professor.idade = data['idade']
    if 'materia' in data:
        professor.materia = data['materia']
    if 'observacoes' in data:
        professor.observacoes = data['observacoes']

    return jsonify(professor.to_dict()), 200

@app.route('/professores/<string:id>', methods=['DELETE'])
def delete_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if professor is None:
        return jsonify({"error": "Professor não encontrado"}), 404

    professores.remove(professor)
    return jsonify({"message": f"Professor com id {id} foi removido com sucesso."}), 200

# CRUD ALUNOS

@app.route('/alunos', methods=['GET'])
def get_alunos_route():
    alunos = get_alunos()  
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    
    required_fields = ['nome', 'idade', 'turma', 'data_nasc', 'nota_primeiro_sem', 'nota_segundo_sem']
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400
    
    turma = next((t for t in get_turmas() if t.id == data['turma']), None)  
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 404
    
    try:
        data_nasc = datetime.strptime(data['data_nasc'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Formato de data de nascimento inválido. Use 'YYYY-MM-DD'"}), 400
    
    aluno = Aluno(len(get_alunos()) + 1, data['nome'], data['idade'], turma, data_nasc, data['nota_primeiro_sem'], data['nota_segundo_sem'])
    
    alunos = get_alunos()  
    alunos.append(aluno)  
    
    return jsonify(aluno.to_dict()), 201

@app.route('/alunos/<int:id>', methods=['GET'])
def aluno(id):
    aluno = get_aluno_by_id(id)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    return jsonify({"error": "Aluno não encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    aluno = next((a for a in get_alunos() if a.id == id), None)  

    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    data = request.get_json()

    if 'nome' in data:
        if not isinstance(data['nome'], str) or len(data['nome'].strip()) == 0:
            return jsonify({"error": "Nome não pode ser vazio ou inválido"}), 400
        aluno.nome = data['nome']
    
    if 'idade' in data:
        if not isinstance(data['idade'], int) or data['idade'] <= 0:
            return jsonify({"error": "Idade deve ser um número inteiro positivo"}), 400
        aluno.idade = data['idade']
    
    if 'turma' in data:
        turma = next((t for t in get_turmas() if t.id == data['turma']), None) 
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        aluno.turma = turma
        aluno.turma_id = turma.id
    
    if 'data_nasc' in data:
        try:
            data_nasc = datetime.strptime(data['data_nasc'], '%Y-%m-%d').date()
            aluno.data_nasc = data_nasc
        except ValueError:
            return jsonify({"error": "Formato de data de nascimento inválido. Use 'YYYY-MM-DD'"}), 400
    
    if 'nota_primeiro_sem' in data:
        if not (0 <= data['nota_primeiro_sem'] <= 10):
            return jsonify({"error": "Nota do primeiro semestre deve estar entre 0 e 10"}), 400
        aluno.nota_primeiro_sem = data['nota_primeiro_sem']
    
    if 'nota_segundo_sem' in data:
        if not (0 <= data['nota_segundo_sem'] <= 10):
            return jsonify({"error": "Nota do segundo semestre deve estar entre 0 e 10"}), 400
        aluno.nota_segundo_sem = data['nota_segundo_sem']
    
    aluno.media_final = (aluno.nota_primeiro_sem + aluno.nota_segundo_sem) / 2

    return jsonify(aluno.to_dict()), 200

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno_removido = remove_aluno(id)  

    if aluno_removido: 
        return jsonify({"message": "Aluno removido com sucesso"}), 200
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404

# CRUD TURMAS

@app.route('/turmas', methods=['GET'])
def get_turmas_route():
    turmas = get_turmas()  
    return jsonify([turma.to_dict() for turma in turmas])

@app.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()

    if not all(key in data for key in ['descricao', 'professor_id', 'ativo']):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400
    
    professor = next((p for p in professores if p.id == data['professor_id']), None)
    
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404
    
    turma = Turma(len(get_turmas()) + 1, data['descricao'], professor, data['ativo'])
    turmas = get_turmas()  
    turmas.append(turma)
    
    return jsonify(turma.to_dict()), 201

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in get_turmas() if t.id == id), None)

    if turma is None:
        return jsonify({"error": "Turma não encontrada"}), 404

    return jsonify(turma.to_dict())

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    turma = next((t for t in get_turmas() if t.id == id), None)

    if turma is None:
        return jsonify({"error": "Turma não encontrada"}), 404

    data = request.get_json()

    if 'descricao' in data:
        turma.descricao = data['descricao']
    if 'professor_id' in data:
        turma.professor_id = data['professor_id']
    if 'ativo' in data:
        turma.ativo = data['ativo']

    return jsonify(turma.to_dict())

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    turma_removido = remove_turma(id)

    if turma_removido:
        return jsonify({"message": "Turma removido com sucesso"}), 200
    else:
        return jsonify({"error": "Turma não encontrado"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)