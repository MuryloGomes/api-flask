from flask import Flask, jsonify, request
from modelos import professores, alunos, turmas, Professor, Aluno, Turma



app = Flask(__name__)

@app.route('/')
def hello():
    return "Seja Bem-vindo!"

@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify([professor.__dict__ for professor in professores])

@app.route('/professores', methods=['POST'])
def add_professor():
    data = request.get_json()
    professor = Professor(len(professores) + 1, data['nome'], data['idade'], data['disciplina'], data['observacoes'])
    professores.append(professor)
    return jsonify(professor.__dict__), 201

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if professor:
        return jsonify(professor.__dict__)
    return jsonify({'message': 'Professor não encontrado'}), 404

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if professor:
        professores.remove(professor)
        return jsonify({'message': 'Professor deletado com sucesso'}), 200
    return jsonify({'message': 'Professor não encontrado'}), 404



@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify([aluno.__dict__ for aluno in alunos])

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    aluno = Aluno(len(alunos) + 1, data['nome'], data['idade'], data['data_nasc'], data['nota_primeiro_sem'], data['nota_segundo_sem'], data['media_final'])
    alunos.append(aluno)
    return jsonify(aluno.__dict__), 201

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in alunos if a.id == id), None)
    if aluno:
        return jsonify(aluno.__dict__)
    return jsonify({'message': 'Aluno não encontrado'}), 404

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = next((a for a in alunos if a.id == id), None)
    if aluno:
        alunos.remove(aluno)
        return jsonify({'message': 'Aluno deletado com sucesso'}), 200
    return jsonify({'message': 'Aluno não encontrado'}), 404



@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify([turma.__dict__ for turma in turmas])

@app.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()
    turma = Turma(len(turmas) + 1, data['nome'], data['professor_id'], data['alunos_ids'], data['ativo'])
    turmas.append(turma)
    return jsonify(turma.__dict__), 201

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in turmas if t.id == id), None)
    if turma:
        return jsonify(turma.__dict__)
    return jsonify({'message': 'Turma não encontrada'}), 404

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.get_json()
    turma = next((t for t in turmas if t.id == id), None)
    if turma:
        turma.nome = data.get('nome', turma.nome)
        turma.professor_id = data.get('professor_id', turma.professor_id)
        turma.alunos_ids = data.get('alunos_ids', turma.alunos_ids)
        turma.ativo = data.get('ativo', turma.ativo)
        return jsonify(turma.__dict__)
    return jsonify({'message': 'Turma não encontrada'}), 404

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    turma = next((t for t in turmas if t.id == id), None)
    if turma:
        turmas.remove(turma)
        return jsonify({'message': 'Turma deletada com sucesso'}), 200
    return jsonify({'message': 'Turma não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)