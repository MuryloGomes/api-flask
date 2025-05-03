from datetime import datetime, date
import uuid
from config import db
from model.turmaModel import Turma

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.String(36), db.ForeignKey('turmas.id'), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    nota_primeiro_sem = db.Column(db.Float, nullable=False)
    nota_segundo_sem = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)

    turma = db.relationship('Turma', backref=db.backref('alunos', lazy=True))

    def __init__(self, nome: str, turma, data_nasc: datetime, nota_primeiro_sem: float, nota_segundo_sem: float):
        if not (0 <= nota_primeiro_sem <= 10) or not (0 <= nota_segundo_sem <= 10):
            raise ValueError("Notas devem estar entre 0 e 10.")
        
        if not isinstance(data_nasc, (datetime, date)):
            raise ValueError("Data de nascimento deve ser um objeto datetime ou date.")

        self.nome = nome
        self.turma = turma
        self.data_nasc = data_nasc
        self.nota_primeiro_sem = nota_primeiro_sem
        self.nota_segundo_sem = nota_segundo_sem
        self.idade = self.calcular_idade()
        self.media_final = (nota_primeiro_sem + nota_segundo_sem) / 2

    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nasc.year - ((today.month, today.day) < (self.data_nasc.month, self.data_nasc.day))

    def to_dict(self):
        return {
            'aluno_id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nasc.strftime('%Y-%m-%d'),
            'nota_primeiro_semestre': self.nota_primeiro_sem,
            'nota_segundo_semestre': self.nota_segundo_sem,
            'media_final': self.media_final
        }

def get_alunos():
    return [aluno.to_dict() for aluno in Aluno.query.all()]

def get_aluno_by_id(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise ValueError(f"Aluno com id {id} não encontrado.")
    return aluno

def remove_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return aluno
    return None

def add_aluno(data):
    turma = Turma.query.get(data['turma'])
    if not turma:
        raise ValueError(f"Turma com id {data['turma']} não encontrada.")
    
    try:
        data_nasc = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Formato de data inválido. Use 'YYYY-MM-DD'.")
    
    aluno = Aluno(
        nome=data['nome'],
        turma=turma,
        data_nasc=data_nasc,
        nota_primeiro_sem=data['nota_primeiro_semestre'],
        nota_segundo_sem=data['nota_segundo_semestre']
    )

    db.session.add(aluno)
    db.session.commit()

    return aluno.to_dict()