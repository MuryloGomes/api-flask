professores = []

class Professor:
    def __init__(self, id: int, nome: str, idade: int, materia: str, observacoes: str):
        self.id = id
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

def add_professor(data):
    professor = Professor(len(professores) + 1, data['nome'], data['idade'], data['materia'], data['observacoes'])
    professores.append(professor)
    return professor