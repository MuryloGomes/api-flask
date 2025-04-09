from flask import Blueprint, request, jsonify
from model.professorModel import Professor, professores, add_professor 

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professores', methods=['GET'])
def get_professores():
    try:
        return jsonify([professor.to_dict() for professor in professores]), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao listar professores: {str(e)}"}), 500

@professor_blueprint.route('/professores', methods=['POST'])
def add_professor_route():
    data = request.get_json()

    required_fields = ['nome', 'idade', 'materia', 'observacoes']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400

    try:
        professor = add_professor(data)
        return jsonify(professor.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar professor: {str(e)}"}), 500

@professor_blueprint.route('/professores/<string:id>', methods=['GET'])
def get_professor(id):
    try:
        professor = next((p for p in professores if p.id == id), None)
        if professor is None:
            return jsonify({"error": "Professor não encontrado"}), 404
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar professor: {str(e)}"}), 500

@professor_blueprint.route('/professores/<string:id>', methods=['PUT'])
def update_professor(id):
    try:
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
    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar professor: {str(e)}"}), 500

@professor_blueprint.route('/professores/<string:id>', methods=['DELETE'])
def delete_professor(id):
    try:
        professor = next((p for p in professores if p.id == id), None)
        if professor is None:
            return jsonify({"error": "Professor não encontrado"}), 404

        professores.remove(professor)
        return jsonify({"message": f"Professor com id {id} foi removido com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao deletar professor: {str(e)}"}), 500