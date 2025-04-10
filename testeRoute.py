import unittest
from app import app
from model.alunoModel import alunos
from model.turmaModel import Turma, turmas
from model.professorModel import Professor, professores


class TestRoutesBlueprint(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        alunos.clear()
        turmas.clear()
        professores.clear()

        self.professor = Professor("Carlos Silva", 45, "Matemática", "Professor experiente")
        professores.append(self.professor)

        self.turma = Turma("Turma A", self.professor, True)
        turmas.append(self.turma)

    def test_01_criar_aluno_valido(self):
        response = self.client.post('/alunos', json={
            "nome": "João da Silva",
            "idade": 17,
            "data_nasc": "2005-06-15",
            "nota_primeiro_sem": 8.0,
            "nota_segundo_sem": 9.0,
            "turma": self.turma.id
        })
        self.assertEqual(response.status_code, 201)

    def test_02_criar_aluno_com_data_errada(self):
        response = self.client.post('/alunos', json={
            "nome": "Maria Souza",
            "idade": 17,
            "data_nasc": "15-06-2005",
            "nota_primeiro_sem": 9.0,
            "nota_segundo_sem": 8.5,
            "turma": self.turma.id
        })
        self.assertEqual(response.status_code, 400)

    def test_03_criar_aluno_faltando_dados(self):
        response = self.client.post('/alunos', json={"nome": "José Oliveira"})
        self.assertEqual(response.status_code, 400)

    def test_04_criar_aluno_com_turma_invalida(self):
        response = self.client.post('/alunos', json={
            "nome": "Camila Dias",
            "idade": 16,
            "data_nasc": "2007-03-22",
            "nota_primeiro_sem": 7.5,
            "nota_segundo_sem": 7.8,
            "turma": "invalid-id"
        })
        self.assertEqual(response.status_code, 404)

    def test_05_listar_alunos_vazio(self):
        response = self.client.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_06_buscar_aluno_existente(self):
        response = self.client.post('/alunos', json={
            "nome": "Lucas Moura",
            "idade": 18,
            "data_nasc": "2006-11-20",
            "nota_primeiro_sem": 9.0,
            "nota_segundo_sem": 9.5,
            "turma": self.turma.id
        })
        aluno_id = response.get_json().get("aluno_id")
        response = self.client.get(f'/alunos/{aluno_id}')
        self.assertEqual(response.status_code, 200)

    def test_07_buscar_aluno_inexistente(self):
        response = self.client.get('/alunos/nao-existe')
        self.assertEqual(response.status_code, 500)

    def test_08_atualizar_aluno_nome_valido(self):
        response = self.client.post('/alunos', json={
            "nome": "Juliana Costa",
            "idade": 16,
            "data_nasc": "2009-02-10",
            "nota_primeiro_sem": 7.0,
            "nota_segundo_sem": 7.5,
            "turma": self.turma.id
        })
        aluno_id = response.get_json().get("aluno_id")
        response = self.client.put(f'/alunos/{aluno_id}', json={"nome": "Juliana Correia"})
        self.assertEqual(response.status_code, 200)

    def test_09_atualizar_aluno_com_turma_nova_valida(self):
        nova_turma = Turma("Turma B", self.professor, True)
        turmas.append(nova_turma)
        response = self.client.post('/alunos', json={
            "nome": "Paulo Mendes",
            "idade": 16,
            "data_nasc": "2008-05-12",
            "nota_primeiro_sem": 6.5,
            "nota_segundo_sem": 7.0,
            "turma": self.turma.id
        })
        aluno_id = response.get_json().get("aluno_id")
        response = self.client.put(f'/alunos/{aluno_id}', json={"turma": nova_turma.id})
        self.assertEqual(response.status_code, 200)

    def test_10_atualizar_aluno_turma_invalida(self):
        response = self.client.post('/alunos', json={
            "nome": "Lívia Lopes",
            "idade": 17,
            "data_nasc": "2007-12-01",
            "nota_primeiro_sem": 9.0,
            "nota_segundo_sem": 8.0,
            "turma": self.turma.id
        })
        aluno_id = response.get_json().get("aluno_id")
        response = self.client.put(f'/alunos/{aluno_id}', json={"turma": "id-invalido"})
        self.assertEqual(response.status_code, 404)

    def test_11_atualizar_com_nota_invalida(self):
        response = self.client.post('/alunos', json={
            "nome": "Fernanda Souza",
            "idade": 17,
            "data_nasc": "2007-09-10",
            "nota_primeiro_sem": 7.0,
            "nota_segundo_sem": 6.5,
            "turma": self.turma.id
        })
        aluno_id = response.get_json().get("aluno_id")
        response = self.client.put(f'/alunos/{aluno_id}', json={"nota_primeiro_sem": 11.0})
        self.assertEqual(response.status_code, 400)

    def test_12_deletar_aluno_existente(self):
        response = self.client.post('/alunos', json={
            "nome": "Vinícius Lima",
            "idade": 17,
            "data_nasc": "2006-08-30",
            "nota_primeiro_sem": 8.5,
            "nota_segundo_sem": 9.0,
            "turma": self.turma.id
        })
        aluno_id = response.get_json().get("aluno_id")
        response = self.client.delete(f'/alunos/{aluno_id}')
        self.assertEqual(response.status_code, 200)

    def test_13_deletar_aluno_inexistente(self):
        response = self.client.delete('/alunos/id-invalido')
        self.assertEqual(response.status_code, 500)

   
    def test_14_criar_professor_valido(self):
        response = self.client.post('/professores', json={
            "nome": "Ana Beatriz",
            "idade": 39,
            "materia": "Português",
            "observacoes": "Didática excelente"
        })
        self.assertEqual(response.status_code, 201)

    def test_15_listar_professores(self):
        response = self.client.get('/professores')
        self.assertEqual(response.status_code, 200)

    def test_16_buscar_professor_existente(self):
        prof = professores[0]
        response = self.client.get(f'/professores/{prof.id}')
        self.assertEqual(response.status_code, 200)

    def test_17_atualizar_professor_valido(self):
        prof = professores[0]
        response = self.client.put(f'/professores/{prof.id}', json={"nome": "Carlos Atualizado"})
        self.assertEqual(response.status_code, 200)

    def test_18_deletar_professor_existente(self):
        novo_prof = Professor("Eliane Nunes", 50, "História", "Muito respeitada")
        professores.append(novo_prof)
        response = self.client.delete(f'/professores/{novo_prof.id}')
        self.assertEqual(response.status_code, 200)

    def test_19_listar_turmas(self):
        response = self.client.get('/turmas')
        self.assertEqual(response.status_code, 200)

    def test_20_buscar_turma_existente(self):
        response = self.client.get(f'/turmas/{self.turma.id}')
        self.assertEqual(response.status_code, 200)

    def test_21_atualizar_turma_valida(self):
        response = self.client.put(f'/turmas/{self.turma.id}', json={"descricao": "Turma Atualizada"})
        self.assertEqual(response.status_code, 200)

    def test_22_deletar_turma_existente(self):
        nova = Turma("Turma Z", self.professor, True)
        turmas.append(nova)
        response = self.client.delete(f'/turmas/{nova.id}')
        self.assertEqual(response.status_code, 200)


    def test_23_criar_professor_valido(self):
        response = self.client.post('/professores', json={
            "nome": "Ana Beatriz",
            "idade": 39,
            "materia": "Português",
            "observacoes": "Didática excelente"
        })
        self.assertEqual(response.status_code, 201)

    def test_24_listar_professores(self):
        response = self.client.get('/professores')
        self.assertEqual(response.status_code, 200)

    def test_25_buscar_professor_existente(self):
        prof = professores[0]
        response = self.client.get(f'/professores/{prof.id}')
        self.assertEqual(response.status_code, 200)

    def test_26_atualizar_professor_valido(self):
        prof = professores[0]
        response = self.client.put(f'/professores/{prof.id}', json={"nome": "Carlos Atualizado"})
        self.assertEqual(response.status_code, 200)
    def test_27_deletar_professor_existente(self):
        novo_prof = Professor("Eliane Nunes", 50, "História", "Muito respeitada")
        professores.append(novo_prof)
        response = self.client.delete(f'/professores/{novo_prof.id}')
        self.assertEqual(response.status_code, 200)

    
    def test_28_listar_turmas(self):
        response = self.client.get('/turmas')
        self.assertEqual(response.status_code, 200)

    def test_29_buscar_turma_existente(self):
        response = self.client.get(f'/turmas/{self.turma.id}')
        self.assertEqual(response.status_code, 200)

    def test_30_atualizar_turma_valida(self):
        response = self.client.put(f'/turmas/{self.turma.id}', json={"descricao": "Turma Atualizada"})
        self.assertEqual(response.status_code, 200)

    def test_31_deletar_turma_existente(self):
        nova = Turma("Turma Z", self.professor, True)
        turmas.append(nova)
        response = self.client.delete(f'/turmas/{nova.id}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
