from datetime import date

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

class Turma:
    def __init__(self, id: int, descricao: str, professor: Professor, ativo: bool):
        self.id = id
        if len(descricao) > 100:
            raise ValueError("A descrição não pode ter mais de 100 caracteres.")
        self.descricao = descricao
        self.professor_id = professor.id
        self.professor = professor
        if not isinstance(ativo, bool):
            raise ValueError("O atributo 'ativo' deve ser um valor booleano (True ou False).")
        self.ativo = ativo

    def to_dict(self):
        return {
            'turma_id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo
        }

class Aluno:
    def __init__(self, id: int, nome: str, idade: int, turma: Turma, data_nasc: date, nota_primeiro_sem: float, nota_segundo_sem: float):
        self.id = id
        if not isinstance(nome, str) or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio.")
        if len(nome) > 100:
            raise ValueError("Nome não pode ter mais de 100 caracteres.")
        
        self.nome = nome
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um número inteiro positivo.")
        
        self.idade = idade
        self.turma_id = turma.id
        self.turma = turma
        self.data_nasc = data_nasc

        if not (0 <= nota_primeiro_sem <= 10):
            raise ValueError("Nota do primeiro semestre deve estar entre 0 e 10.")
        self.nota_primeiro_sem = nota_primeiro_sem
        
        if not (0 <= nota_segundo_sem <= 10):
            raise ValueError("Nota do segundo semestre deve estar entre 0 e 10.")
        self.nota_segundo_sem = nota_segundo_sem
        self.media_final = (nota_primeiro_sem + nota_segundo_sem) / 2

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

professores = [
    Professor(1, "Dr. Joao Silva", 45, "Matematica", "Excelente professor."),
    Professor(2, "Profa. Ana Souza", 38, "Fisica", "Professor dedicada."),
    Professor(3, "Dr. Carlos Lima", 50, "Quimica", "Grande experiencia em laboratorios."),
    Professor(4, "Profa. Maria Costa", 40, "Biologia", "Com vasto conhecimento academico."),
    Professor(5, "Dr. Pedro Almeida", 55, "Literatura", "Especialista em literatura moderna.")
]

turmas = [
    Turma(1, "Turma A - 1º Semestre", professores[0], True),
    Turma(2, "Turma B - 1º Semestre", professores[1], True),
    Turma(3, "Turma C - 1º Semestre", professores[2], False),
    Turma(4, "Turma D - 1º Semestre", professores[3], True),
    Turma(5, "Turma E - 1º Semestre", professores[4], False)
]

alunos = [
    Aluno(1, "Carlos Silva", 20, turmas[0], date(2003, 5, 20), 8.5, 9.0),
    Aluno(2, "Maria Oliveira", 22, turmas[1], date(2001, 11, 15), 7.0, 6.5),
    Aluno(3, "Joao Santos", 19, turmas[2], date(2004, 2, 10), 9.5, 8.0),
    Aluno(4, "Ana Costa", 21, turmas[3], date(2002, 8, 3), 6.0, 7.0),
    Aluno(5, "Pedro Lima", 23, turmas[4], date(2000, 9, 30), 8.0, 8.5)
]
