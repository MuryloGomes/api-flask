professores = []
alunos = []
turmas = []

class Professor:
    def __init__(self, id, nome, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina

class Aluno:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

class Turma:
    def __init__(self, id, nome, professor_id, alunos_ids):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id
        self.alunos_ids = alunos_ids