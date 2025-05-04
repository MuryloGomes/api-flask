from flask_restx import Namespace, Resource, fields
from model.professorModel import get_professores, add_professor, get_professor_by_id, remove_professor

# Criação do namespace "professores"
professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

# Definição do modelo para as entradas de dados do professor
professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor", max_length=100),
    "idade": fields.Integer(required=True, description="Idade do professor"),
    "materia": fields.String(required=True, description="Matéria que o professor leciona", max_length=100),
    "observacoes": fields.String(description="Observações sobre o professor")
})

# Definição do modelo para a saída de dados do professor
professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.String(description="ID do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "materia": fields.String(description="Matéria que o professor leciona"),
    "nome": fields.String(description="Nome do professor"),
    "observacoes": fields.String(description="Observações sobre o professor")
})

# Recurso para listar e adicionar professores
@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return get_professores()

    @professores_ns.expect(professor_model)
    def post(self):
        """Cria um novo professor"""
        data = professores_ns.payload
        response = add_professor(data)
        return response, 201  # Retorna o professor criado com status 201

# Recurso para operações em um único professor pelo ID
@professores_ns.route("/<string:id_professor>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return get_professor_by_id(id_professor)

    @professores_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professores_ns.payload
        atualizar_professor = remove_professor(id_professor)
        response = add_professor(data)
        return response, 200

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        response = remove_professor(id_professor)
        if response:
            return {"message": "Professor excluído com sucesso"}, 200
        return {"message": "Professor não encontrado"}, 404