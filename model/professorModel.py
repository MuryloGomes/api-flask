import uuid

professores = []

class Professor:
    def __init__(self, nome: str, idade: int, materia: str, observacoes: str):
        self.id = str(uuid.uuid4())  
        if len(nome) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")
        self.nome = nome
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um número inteiro positivo.")
        self.idade = idade
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

def add_professor(data):
    professor = Professor(data['nome'], data['idade'], data['materia'], data['observacoes'])
    professores.append(professor)
    return professor