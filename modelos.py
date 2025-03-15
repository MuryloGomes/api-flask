from datetime import date

class Professor:
    def __init__(self, id: int, nome: str, idade: int, materia: str, observacoes: str):
        self.id = id
        if len(nome) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")
        self.nome = nome
        if not isinstance(idade, int):
            raise ValueError("A 'idade' deve ser um número inteiro.")
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

class Aluno:
    def __init__(self, id: int, nome: str, idade: int, data_nasc: date, nota_primeiro_sem: float, nota_segundo_sem: float):
        self.id = id
        if not isinstance(nome, str) or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio.")
        if len(nome) > 100:
            raise ValueError("Nome não pode ter mais de 100 caracteres.")
        
        self.nome = nome
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um número inteiro positivo.")
        
        self.idade = idade
        self.data_nasc = data_nasc

        if not (0 <= nota_primeiro_sem <= 10):
            raise ValueError("Nota do primeiro semestre deve estar entre 0 e 10.")
        self.nota_primeiro_sem = nota_primeiro_sem
        
        if not (0 <= nota_segundo_sem <= 10):
            raise ValueError("Nota do segundo semestre deve estar entre 0 e 10.")
        self.nota_segundo_sem = nota_segundo_sem
        self.media_final = (nota_primeiro_sem + nota_segundo_sem) / 2

professores = [
    Professor(1, "Dr. João Silva", 45, "Matemática", "Excelente professor."),
    Professor(2, "Profa. Ana Souza", 38, "Física", "Professor dedicada."),
    Professor(3, "Dr. Carlos Lima", 50, "Química", "Grande experiência em laboratórios."),
    Professor(4, "Profa. Maria Costa", 40, "Biologia", "Com vasto conhecimento acadêmico."),
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
    Aluno(1, "Carlos Silva", 20, date(2003, 5, 20), 8.5, 9.0),
    Aluno(2, "Maria Oliveira", 22, date(2001, 11, 15), 7.0, 6.5),
    Aluno(3, "João Santos", 19, date(2004, 2, 10), 9.5, 8.0),
    Aluno(4, "Ana Costa", 21, date(2002, 8, 3), 6.0, 7.0),
    Aluno(5, "Pedro Lima", 23, date(2000, 9, 30), 8.0, 8.5)
]