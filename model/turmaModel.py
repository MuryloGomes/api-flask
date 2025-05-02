import uuid
from config import db
from model.professorModel import Professor

class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.String(36), db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    professor = db.relationship('Professor', backref=db.backref('turmas', lazy=True))

    def __init__(self, descricao: str, professor, ativo: bool):
        if len(descricao) > 100:
            raise ValueError("A descrição não pode ter mais de 100 caracteres.")
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        return {
            'turma_id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo
        }

# Funções auxiliares (CRUD)
def get_turmas():
    return [t.to_dict() for t in Turma.query.all()]

def get_turma_by_id(id):
    turma = Turma.query.get(id)
    return turma

def remove_turma(id):
    turma = Turma.query.get(id)
    if turma:
        db.session.delete(turma)
        db.session.commit()
        return turma
    return None

def add_turma(data):
    professor = Professor.query.get(data['professor_id'])
    if not professor:
        raise ValueError("Professor não encontrado.")
    
    turma = Turma(descricao=data['descricao'], professor=professor, ativo=data['ativo'])
    db.session.add(turma)
    db.session.commit()
    return turma.to_dict()