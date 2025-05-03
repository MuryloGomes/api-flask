from flask_restx import Namespace, Resource, fields
from model.alunoModel import get_alunos, get_aluno_by_id, add_aluno, remove_aluno

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

aluno_model = alunos_ns.model("Aluno", {
    "nome": fields.String(required=True, description="Nome do aluno", max_length=100),
    "data_nasc": fields.String(required=True, description="Data de nascimento no formato YYYY-MM-DD"),
    "nota_primeiro_sem": fields.Float(required=True, description="Nota do primeiro semestre (0 a 10)"),
    "nota_segundo_sem": fields.Float(required=True, description="Nota do segundo semestre (0 a 10)"),
    "turma": fields.String(required=True, description="ID da turma associada"),
})

aluno_output_model = alunos_ns.model("AlunoOutput", {
    "aluno_id": fields.String(description="ID do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento"),
    "idade": fields.Integer(description="Idade do aluno"),
    "media_final": fields.Float(description="Média final do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "turma_id": fields.String(description="ID da turma associada"),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        return get_alunos()

    @alunos_ns.expect(aluno_model)
    def post(self):
        data = alunos_ns.payload
        try:
            response = add_aluno(data)
            return response, 201
        except ValueError as e:
            return {"message": str(e)}, 400

@alunos_ns.route("/<string:id_aluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        try:
            aluno = get_aluno_by_id(id_aluno)
            return aluno.to_dict(), 200
        except ValueError:
            return {"message": "Aluno não encontrado"}, 404

    @alunos_ns.expect(aluno_model)
    def put(self, id_aluno):
        aluno = get_aluno_by_id(id_aluno)
        if not aluno:
            return {"message": "Aluno não encontrado"}, 404
        try:
            data = alunos_ns.payload
            remove_aluno(id_aluno)
            novo_aluno = add_aluno(data)
            return novo_aluno, 200
        except ValueError as e:
            return {"message": str(e)}, 400

    def delete(self, id_aluno):
        aluno = remove_aluno(id_aluno)
        if not aluno:
            return {"message": "Aluno não encontrado"}, 404
        return {"message": "Aluno excluído com sucesso"}, 200