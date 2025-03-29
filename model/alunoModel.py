from datetime import date

alunos = []

def get_turmas():
    from model.turmaModel import get_turmas 
    return get_turmas()

class Aluno:
    def __init__(self, id: int, nome: str, idade: int, turma, data_nasc: date, nota_primeiro_sem: float, nota_segundo_sem: float):
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

def get_alunos():
    global alunos
    turmas = get_turmas() 
    alunos = [
        Aluno(1, "Carlos Silva", 20, turmas[0], date(2003, 5, 20), 8.5, 9.0),
        Aluno(2, "Maria Oliveira", 22, turmas[1], date(2001, 11, 15), 7.0, 6.5),
        Aluno(3, "Joao Santos", 19, turmas[2], date(2004, 2, 10), 9.5, 8.0),
        Aluno(4, "Ana Costa", 21, turmas[3], date(2002, 8, 3), 6.0, 7.0),
        Aluno(5, "Pedro Lima", 23, turmas[4], date(2000, 9, 30), 8.0, 8.5)
    ]
    return alunos

def get_aluno_by_id(id):
    alunos = get_alunos()  
    aluno = next((a for a in alunos if a.id == id), None) 
    return aluno

def remove_aluno(id):
    alunos = get_alunos()
    aluno = next((a for a in alunos if a.id == id), None) 
    
    if aluno:
        alunos = [a for a in alunos if a.id != id] 
        return aluno  
    else:
        return None 