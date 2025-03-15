class Professor:
    def __init__(self, id, nome, idade, disciplina, observacoes, turma_id):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina
        self.observacoes = observacoes
        self.turma_id = turma_id
        '''TIRAR TURMA ID'''

class Aluno:
    def __init__(self, id, nome, idade, data_nasc, nota_primeiro_sem, nota_segundo_sem, media_final):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.data_nasc = data_nasc
        self.nota_primeiro_sem = nota_primeiro_sem
        self.nota_segundo_sem = nota_segundo_sem
        self.media_final = media_final
        '''ADICIONAR TURMA ID'''

class Turma:
    def __init__(self, id, nome, professor_id, alunos_ids, ativo):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id
        self.alunos_ids = alunos_ids
        self.ativo = ativo
        '''TIRAR ALUNOS IDS'''

professores = [
    Professor(1, "João", 26, "Matemática"),
    Professor(2, "Maria", 49, "Física"),
    Professor(3, "Carlos", 53, "Química")
]

alunos = [
    Aluno(1, "Ana Souza", 20, '12/02/2006', 5.5, 6.8, 6,1),
    Aluno(2, "Carlos Silva", 22, '22/05/2007', 7.0, 6,5, 6,7),
    Aluno(3, "Lucas Oliveira", 21, '11/10/2006', 8.5, 7.2, 7,8),
    Aluno(4, "Maria Santos", 23, '20/01/2007', 4.5, 9.5, 7,0),
    Aluno(5, "Juliana Pereira", 19, '21/09/2006'/ 6.8, 9.1, 7,9)
]

turmas = [
    Turma(1, "Turma A - 2025/1", 1, [1, 2, 3], ativo=True),  
    Turma(2, "Turma B - 2025/1", 2, [3, 4, 5], ativo=False),
    Turma(3, "Turma A - 2025/2", 1, [1, 4], ativo=True),    
    Turma(4, "Turma B - 2025/2", 3, [2, 5], ativo=True)     
]