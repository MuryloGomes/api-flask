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

professores = [
    Professor(1, "Dr. Joao Silva", 45, "Matematica", "Excelente professor."),
    Professor(2, "Profa. Ana Souza", 38, "Fisica", "Professor dedicada."),
    Professor(3, "Dr. Carlos Lima", 50, "Quimica", "Grande experiencia em laboratorios."),
    Professor(4, "Profa. Maria Costa", 40, "Biologia", "Com vasto conhecimento academico."),
    Professor(5, "Dr. Pedro Almeida", 55, "Literatura", "Especialista em literatura moderna.")
]