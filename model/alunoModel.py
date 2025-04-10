import uuid
from datetime import date, datetime

alunos = []

def get_turmas():
    from model.turmaModel import get_turmas
    return get_turmas()

class Aluno:
    def __init__(self, nome: str, idade: int, turma, data_nasc: date, nota_primeiro_sem: float, nota_segundo_sem: float):
        self.id = str(uuid.uuid4())  
        try:
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
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Erro ao criar aluno: {str(e)}")

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
    return alunos

def get_aluno_by_id(id):
    try:
        aluno = next((a for a in get_alunos() if a.id == id), None)
        if aluno is None:
            raise ValueError(f"Aluno com id {id} não encontrado.")
        return aluno
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise Exception(f"Erro ao buscar aluno: {str(e)}")

def remove_aluno(id):
    try:
        aluno = next((a for a in get_alunos() if a.id == id), None)
        if aluno:
            alunos.remove(aluno)
            return aluno
        else:
            raise ValueError(f"Aluno com id {id} não encontrado.")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise Exception(f"Erro ao remover aluno: {str(e)}")

def add_aluno(data):
    try:
        turma = next((t for t in get_turmas() if t.id == data['turma']), None)
        
        if not turma:
            raise ValueError(f"Turma com id {data['turma']} não encontrada.")
        
        try:
            data_nasc = datetime.strptime(data['data_nasc'], '%Y-%m-%d').date()
        except ValueError as ve:
            raise ValueError(f"Formato de data de nascimento inválido. Use 'YYYY-MM-DD'. Detalhes: {str(ve)}")
        
        aluno = Aluno(data['nome'], data['idade'], turma, data_nasc, data['nota_primeiro_sem'], data['nota_segundo_sem'])
        alunos.append(aluno)
        return aluno
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise Exception(f"Erro ao adicionar aluno: {str(e)}")
