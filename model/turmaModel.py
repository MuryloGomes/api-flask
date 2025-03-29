def get_professor():
    from professorModel import professores  
    return professores  

class Turma:
    def __init__(self, id: int, descricao: str, professor, ativo: bool):
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

def get_turmas():
    professores = get_professor()
    turmas = [
        Turma(1, "Turma A - 1º Semestre", professores[0], True),
        Turma(2, "Turma B - 1º Semestre", professores[1], True),
        Turma(3, "Turma C - 1º Semestre", professores[2], False),
        Turma(4, "Turma D - 1º Semestre", professores[3], True),
        Turma(5, "Turma E - 1º Semestre", professores[4], False)
    ]
    return turmas

def get_turma_by_id(id):
    turmas = get_turmas()  
    turma = next((a for a in turmas if a.id == id), None) 
    return turma

def remove_turma(id):
    turmas = get_turmas()
    turma_removida = [turma for turma in turmas if turma.id == id]
    
    if turma_removida:
        turmas = [turma for turma in turmas if turma.id != id]
        return turma_removida[0]  
    return None 