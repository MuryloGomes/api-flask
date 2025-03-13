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

professores = [
    Professor(1, "João", "Matemática"),
    Professor(2, "Maria", "Física"),
    Professor(3, "Carlos", "Química")
]

alunos = [
    Aluno(1, "Ana Souza", 20),
    Aluno(2, "Carlos Silva", 22),
    Aluno(3, "Lucas Oliveira", 21),
    Aluno(4, "Maria Santos", 23),
    Aluno(5, "Juliana Pereira", 19)
]

turmas = [
    Turma(1, "Turma A - 2025/1", 1, [1, 2, 3]),  
    Turma(2, "Turma B - 2025/1", 2, [3, 4, 5]),
    Turma(3, "Turma A - 2025/2", 1, [1, 4]),    
    Turma(4, "Turma B - 2025/2", 3, [2, 5])     
]