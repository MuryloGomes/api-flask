from flask import Blueprint, request, jsonify
from model.turmaModel import Turma, get_turmas, get_turma_by_id, remove_turma, add_turma 
from model.professorModel import professores

turma_blueprint = Blueprint('turma', __name__)

@turma_blueprint.route('/turmas', methods=['GET'])
def get_turmas_route():
    try:
        turmas = get_turmas()  
        if not turmas:
            return jsonify({"error": "Nenhuma turma encontrada"}), 404
        return jsonify([turma.to_dict() for turma in turmas]), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao listar turmas: {str(e)}"}), 500

@turma_blueprint.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()
 
    required_fields = ['descricao', 'professor_id', 'ativo']
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400

    try:
        # Validação adicional para o campo de descrição
        if len(data['descricao']) > 100:
            return jsonify({"error": "Descrição não pode ter mais de 100 caracteres"}), 400
        
        professor = next((p for p in professores if p.id == data['professor_id']), None)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
     
        turma = Turma(data['descricao'], professor, data['ativo'])
        turmas = get_turmas()  
        turmas.append(turma)
 
        return jsonify(turma.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar turma: {str(e)}"}), 500

@turma_blueprint.route('/turmas/<string:id>', methods=['GET'])
def get_turma(id):
    try:
        turma = get_turma_by_id(id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        return jsonify(turma.to_dict()), 200
    except ValueError as ve:
        return jsonify({"error": f"Valor inválido: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao buscar turma: {str(e)}"}), 500

@turma_blueprint.route('/turmas/<string:id>', methods=['PUT'])
def update_turma(id):
    data = request.get_json()
    
    try:
        if 'descricao' in data and len(data['descricao']) > 100:
            return jsonify({"error": "Descrição não pode ter mais de 100 caracteres"}), 400
        
        turma = get_turma_by_id(id)
        if not turma:
            return jsonify({"error": f"Turma com id {id} não encontrada"}), 404

        if 'descricao' in data:
            turma.descricao = data['descricao']

        if 'professor_id' in data:
            professor = next((p for p in professores if p.id == data['professor_id']), None)
            if not professor:
                return jsonify({"error": "Professor não encontrado"}), 404
            turma.professor = professor 
            turma.professor_id = professor.id 
        
        if 'ativo' in data:
            turma.ativo = data['ativo']
        
        return jsonify(turma.to_dict()), 200
    
    except KeyError as e:
        return jsonify({"error": f"Campo ausente: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar turma: {str(e)}"}), 500

@turma_blueprint.route('/turmas/<string:id>', methods=['DELETE'])
def delete_turma(id):
    try:
        turma_removida = remove_turma(id)
        if not turma_removida:
            return jsonify({"error": "Turma não encontrada"}), 404
        return jsonify({"message": f"Turma com id {id} foi removida com sucesso."}), 200
    except ValueError as ve:
        return jsonify({"error": f"Valor inválido: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao deletar turma: {str(e)}"}), 500
