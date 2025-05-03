from flask import Blueprint, request, jsonify
from datetime import datetime, date
from model.alunoModel import Aluno
from model.turmaModel import Turma
from config import db

aluno_blueprint = Blueprint('aluno', __name__)

@aluno_blueprint.route('/alunos', methods=['GET'])
def get_alunos_route():
    try:
        alunos = Aluno.query.all()
        return jsonify([aluno.to_dict() for aluno in alunos]), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao listar alunos: {str(e)}"}), 500

@aluno_blueprint.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()

    required_fields = ['nome', 'turma', 'data_nasc', 'nota_primeiro_sem', 'nota_segundo_sem']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltam dados obrigatórios"}), 400

    try:
        turma = Turma.query.get(data['turma'])
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404

        try:
            data_nasc = datetime.strptime(data['data_nasc'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Formato de data de nascimento inválido. Use 'YYYY-MM-DD'"}), 400

        nota1 = data['nota_primeiro_sem']
        nota2 = data['nota_segundo_sem']
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            return jsonify({"error": "Notas devem estar entre 0 e 10"}), 400

        aluno = Aluno(
            nome=data['nome'],
            turma=turma,
            data_nasc=data_nasc,
            nota_primeiro_sem=nota1,
            nota_segundo_sem=nota2
        )

        db.session.add(aluno)
        db.session.commit()

        return jsonify(aluno.to_dict()), 201

    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar aluno: {str(e)}"}), 500

@aluno_blueprint.route('/alunos/<string:id>', methods=['GET'])
def aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if aluno:
            return jsonify(aluno.to_dict()), 200
        return jsonify({"error": "Aluno não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar aluno: {str(e)}"}), 500

@aluno_blueprint.route('/alunos/<string:id>', methods=['PUT'])
def update_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404

        data = request.get_json()

        if 'nome' in data and isinstance(data['nome'], str) and data['nome'].strip():
            aluno.nome = data['nome']

        if 'turma' in data:
            turma = Turma.query.get(data['turma'])
            if not turma:
                return jsonify({"error": "Turma não encontrada"}), 404
            aluno.turma = turma

        if 'data_nasc' in data:
            try:
                aluno.data_nasc = datetime.strptime(data['data_nasc'], '%Y-%m-%d').date()
                today = date.today()
                aluno.idade = today.year - aluno.data_nasc.year - ((today.month, today.day) < (aluno.data_nasc.month, aluno.data_nasc.day))
            except ValueError:
                return jsonify({"error": "Formato de data inválido. Use 'YYYY-MM-DD'"}), 400

        if 'nota_primeiro_sem' in data and 0 <= data['nota_primeiro_sem'] <= 10:
            aluno.nota_primeiro_sem = data['nota_primeiro_sem']

        if 'nota_segundo_sem' in data and 0 <= data['nota_segundo_sem'] <= 10:
            aluno.nota_segundo_sem = data['nota_segundo_sem']

        aluno.media_final = (aluno.nota_primeiro_sem + aluno.nota_segundo_sem) / 2

        db.session.commit()
        return jsonify(aluno.to_dict()), 200

    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar aluno: {str(e)}"}), 500

@aluno_blueprint.route('/alunos/<string:id>', methods=['DELETE'])
def delete_aluno(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404

        db.session.delete(aluno)
        db.session.commit()
        return jsonify({"message": "Aluno removido com sucesso"}), 200

    except Exception as e:
        return jsonify({"error": f"Erro ao deletar aluno: {str(e)}"}), 500