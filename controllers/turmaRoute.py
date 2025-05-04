from flask import Blueprint, request, jsonify
from model.turmaModel import Turma
from model.professorModel import Professor
from config import db

turma_blueprint = Blueprint('turma', __name__)

@turma_blueprint.route('/turmas', methods=['GET'])
def get_turmas_route():
    try:
        turmas = Turma.query.all()
        if not turmas:
            return jsonify({"error": "Nenhuma turma encontrada"}), 404
        return jsonify([turma.to_dict() for turma in turmas]), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao listar turmas: {str(e)}"}), 500


@turma_blueprint.route('/turmas', methods=['POST'])
def add_turma_route():
    data = request.get_json()

    required_fields = ['descricao', 'professor_id', 'ativo']
    if not all(key in data for key in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400

    try:
        if len(data['descricao']) > 100:
            return jsonify({"error": "Descrição não pode ter mais de 100 caracteres"}), 400

        if not isinstance(data['ativo'], bool):
            return jsonify({"error": "O campo 'ativo' deve ser booleano"}), 400

        professor = Professor.query.get(data['professor_id'])
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404

        turma = Turma(
            descricao=data['descricao'],
            professor=professor,  # Corrigido aqui
            ativo=data['ativo']
        )
        db.session.add(turma)
        db.session.commit()

        return jsonify(turma.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar turma: {str(e)}"}), 500


@turma_blueprint.route('/turmas/<string:id>', methods=['GET'])
def get_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        return jsonify(turma.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar turma: {str(e)}"}), 500


@turma_blueprint.route('/turmas/<string:id>', methods=['PUT'])
def update_turma(id):
    try:
        data = request.get_json()

        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404

        if 'descricao' in data:
            if len(data['descricao']) > 100:
                return jsonify({"error": "Descrição não pode ter mais de 100 caracteres"}), 400
            turma.descricao = data['descricao']

        if 'professor_id' in data:
            professor = Professor.query.get(data['professor_id'])
            if not professor:
                return jsonify({"error": "Professor não encontrado"}), 404
            turma.professor = professor

        if 'ativo' in data:
            if not isinstance(data['ativo'], bool):
                return jsonify({"error": "O campo 'ativo' deve ser booleano"}), 400
            turma.ativo = data['ativo']

        db.session.commit()
        return jsonify(turma.to_dict()), 200

    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar turma: {str(e)}"}), 500


@turma_blueprint.route('/turmas/<string:id>', methods=['DELETE'])
def delete_turma(id):
    try:
        turma = Turma.query.get(id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404

        db.session.delete(turma)
        db.session.commit()
        return jsonify({"message": f"Turma com id {id} foi removida com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao deletar turma: {str(e)}"}), 500