from flask_restx import Namespace, Resource, fields
from model.turmaModel import get_turmas, add_turma, get_turma_by_id, remove_turma

turmas_ns = Namespace("turmas", description="Operações relacionadas às turmas")

# Modelo de entrada
turma_model = turmas_ns.model("Turma", {
    "descricao": fields.String(required=True, description="Descrição da turma", max_length=100),
    "professor_id": fields.String(required=True, description="ID do professor associado à turma"),
    "ativo": fields.Boolean(required=True, description="Status da turma (ativa ou inativa)"),
})

# Modelo de saída
turma_output_model = turmas_ns.model("TurmaOutput", {
    "ativo": fields.Boolean(description="Status da turma (ativa ou inativa)"),
    "descricao": fields.String(description="Descrição da turma"),
    "professor_id": fields.String(description="ID do professor associado à turma"),
    "turma_id": fields.String(description="ID da turma"),
})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return get_turmas()

    @turmas_ns.expect(turma_model)
    def post(self):
        """Cria uma nova turma"""
        data = turmas_ns.payload
        response = add_turma(data)
        return response, 201

@turmas_ns.route("/<string:id_turma>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        turma = get_turma_by_id(id_turma)
        if not turma:
            return {"message": "Turma não encontrada"}, 404
        return turma.to_dict(), 200

    @turmas_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza uma turma pelo ID (substituindo)"""
        # Estratégia de "atualização simulada"
        turma = remove_turma(id_turma)
        if not turma:
            return {"message": "Turma não encontrada"}, 404
        data = turmas_ns.payload
        response = add_turma(data)
        return response, 200

    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        turma = remove_turma(id_turma)
        if not turma:
            return {"message": "Turma não encontrada"}, 404
        return {"message": "Turma excluída com sucesso"}, 200
