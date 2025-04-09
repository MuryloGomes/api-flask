from flask import Blueprint, request, jsonify
from datetime import datetime
from model.turmaModel import get_turmas
from model.alunoModel import Aluno, get_alunos, get_aluno_by_id, remove_aluno  

aluno_blueprint = Blueprint('aluno', __name__)

@aluno_blueprint.route('/alunos', methods=['GET'])
def get_alunos_route():
    try:
        alunos = get_alunos()  
        return jsonify([aluno.to_dict() for aluno in alunos])
    except Exception as e:
        return jsonify({"error": f"Erro ao listar alunos: {str(e)}"}), 500

@aluno_blueprint.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    
    required_fields = ['nome', 'idade', 'turma', 'data_nasc', 'nota_primeiro_sem', 'nota_segundo_sem']
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400
    
    try:
        turma = next((t for t in get_turmas() if t.id == data['turma']), None)  
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        
        data_nasc = datetime.strptime(data['data_nasc'], '%Y-%m-%d').date()
        
        aluno = Aluno(data['nome'], data['idade'], turma, data_nasc, data['nota_primeiro_sem'], data['nota_segundo_sem'])
        alunos = get_alunos()  
        alunos.append(aluno)  
        
        return jsonify(aluno.to_dict()), 201
    except ValueError:
        return jsonify({"error": "Formato de data de nascimento inválido. Use 'YYYY-MM-DD'"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar aluno: {str(e)}"}), 500

@aluno_blueprint.route('/alunos/<string:id>', methods=['GET'])
def aluno(id):
    try:
        aluno = get_aluno_by_id(id)
        if aluno:
            return jsonify(aluno.to_dict()), 200
        return jsonify({"error": "Aluno não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar aluno: {str(e)}"}), 500

@aluno_blueprint.route('/alunos/<string:id>', methods=['PUT'])
def update_aluno(id):
    try:
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
    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar aluno: {str(e)}"}), 500

@aluno_blueprint.route('/alunos/<string:id>', methods=['DELETE'])
def delete_aluno(id):
    try:
        aluno_removido = remove_aluno(id)  
        if aluno_removido: 
            return jsonify({"message": "Aluno removido com sucesso"}), 200
        else:
            return jsonify({"error": "Aluno não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao deletar aluno: {str(e)}"}), 500