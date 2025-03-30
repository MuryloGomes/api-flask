def get_professor():
    from professorModel import professores  
    return professores  

turmas = []

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
    return turmas

def get_turma_by_id(id):
    turmas = get_turmas()  
    turma = next((a for a in turmas if a.id == id), None) 
    return turma

def remove_turma(id):
    turma = next((a for a in turmas if a.id == id), None)
    
    if turma:
        turmas.remove(turma)
        return turma
    else:
        return None
    
def add_turma(data):
    professor = next((p for p in get_professor() if p.id == data['professor_id']), None)
    
    if not professor:
        return None
    
    turma = Turma(len(turmas) + 1, data['descricao'], professor, data['ativo'])
    
    turmas.append(turma)

    return turma.to_dict()
