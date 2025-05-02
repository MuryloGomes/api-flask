from flask import Blueprint, request, jsonify
from model.professorModel import Professor
from config import db

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professores', methods=['GET'])
def get_professores():
    try:
        professores = Professor.query.all()
        if not professores:
            return jsonify({"error": "Nenhum professor encontrado"}), 404
        return jsonify([prof.to_dict() for prof in professores]), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao listar professores: {str(e)}"}), 500


@professor_blueprint.route('/professores', methods=['POST'])
def add_professor_route():
    data = request.get_json()

    required_fields = ['nome', 'idade', 'materia', 'observacoes']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400

    try:
        if not isinstance(data['nome'], str) or len(data['nome'].strip()) == 0:
            return jsonify({"error": "Nome inválido"}), 400
        if not isinstance(data['idade'], int) or data['idade'] <= 0:
            return jsonify({"error": "Idade inválida"}), 400
        if not isinstance(data['materia'], str) or len(data['materia'].strip()) == 0:
            return jsonify({"error": "Matéria inválida"}), 400
        if not isinstance(data['observacoes'], str):
            return jsonify({"error": "Observações devem ser uma string"}), 400

        professor = Professor(
            nome=data['nome'],
            idade=data['idade'],
            materia=data['materia'],
            observacoes=data['observacoes']
        )
        db.session.add(professor)
        db.session.commit()

        return jsonify(professor.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar professor: {str(e)}"}), 500


@professor_blueprint.route('/professores/<string:id>', methods=['GET'])
def get_professor(id):
    try:
        professor = Professor.query.get(id)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar professor: {str(e)}"}), 500


@professor_blueprint.route('/professores/<string:id>', methods=['PUT'])
def update_professor(id):
    try:
        professor = Professor.query.get(id)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404

        data = request.get_json()

        if 'nome' in data:
            if not isinstance(data['nome'], str) or len(data['nome'].strip()) == 0:
                return jsonify({"error": "Nome inválido"}), 400
            professor.nome = data['nome']
        if 'idade' in data:
            if not isinstance(data['idade'], int) or data['idade'] <= 0:
                return jsonify({"error": "Idade inválida"}), 400
            professor.idade = data['idade']
        if 'materia' in data:
            if not isinstance(data['materia'], str) or len(data['materia'].strip()) == 0:
                return jsonify({"error": "Matéria inválida"}), 400
            professor.materia = data['materia']
        if 'observacoes' in data:
            if not isinstance(data['observacoes'], str):
                return jsonify({"error": "Observações devem ser uma string"}), 400
            professor.observacoes = data['observacoes']

        db.session.commit()
        return jsonify(professor.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar professor: {str(e)}"}), 500


@professor_blueprint.route('/professores/<string:id>', methods=['DELETE'])
def delete_professor(id):
    try:
        professor = Professor.query.get(id)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404

        db.session.delete(professor)
        db.session.commit()
        return jsonify({"message": f"Professor com id {id} foi removido com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao deletar professor: {str(e)}"}), 500