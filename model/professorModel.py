import uuid
from config import db

class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text)

    def __init__(self, nome: str, idade: int, materia: str, observacoes: str):
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio.")
        if len(nome) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")
        self.nome = nome

        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um número inteiro positivo.")
        self.idade = idade

        if not materia or len(materia.strip()) == 0:
            raise ValueError("Matéria não pode ser vazia.")
        if len(materia) > 100:
            raise ValueError("A matéria não pode ter mais de 100 caracteres.")
        self.materia = materia

        self.observacoes = observacoes

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes
        }

# Funções auxiliares (CRUD)
def add_professor(data):
    professor = Professor(
        nome=data['nome'],
        idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes', '')
    )
    db.session.add(professor)
    db.session.commit()
    return professor.to_dict()

def get_professores():
    return [p.to_dict() for p in Professor.query.all()]

def get_professor_by_id(id):
    professor = Professor.query.get(id)
    if not professor:
        raise ValueError(f"Professor com id {id} não encontrado.")
    return professor.to_dict()

def remove_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        raise ValueError(f"Professor com id {id} não encontrado.")
    db.session.delete(professor)
    db.session.commit()
    return professor.to_dict()