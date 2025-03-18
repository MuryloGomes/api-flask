import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        # Configura o cliente de teste do Flask
        self.app = app.test_client()
        self.app.testing = True

    # Teste 1: Adicionar um professor
    def test_001_add_professor(self):
        professor_data = {
            'nome': 'John Doe',
            'idade': 30,
            'disciplina': 'Matemática',
            'observacoes': 'Muito bom!'
        }
        response = self.app.post('/professores', json=professor_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)  
        self.assertEqual(response.json['nome'], 'John Doe')

    # Teste 2: Buscar todos os professores
    def test_002_get_professores(self):
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    # Teste 3: Buscar professor por ID
    def test_003_get_professor(self):
        professor_data = {
            'nome': 'Jane Smith',
            'idade': 35,
            'disciplina': 'Física',
            'observacoes': 'Muito experiente!'
        }
        response = self.app.post('/professores', json=professor_data)
        professor_id = response.json['id']
        response = self.app.get(f'/professores/{professor_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Jane Smith')

    # Teste 4: Atualizar professor
    def test_004_update_professor(self):
        professor_data = {
            'nome': 'Carlos Silva',
            'idade': 40,
            'disciplina': 'Química',
            'observacoes': 'Exímio!'
        }
        response = self.app.post('/professores', json=professor_data)
        professor_id = response.json['id']
        
        update_data = {
            'nome': 'Carlos Silva Neto',
            'idade': 41,
            'disciplina': 'Química',
            'observacoes': 'Excelente!'
        }
        response = self.app.put(f'/professores/{professor_id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Carlos Silva Neto')

    # Teste 5: Deletar professor
    def test_005_delete_professor(self):
        professor_data = {
            'nome': 'Ana Souza',
            'idade': 50,
            'disciplina': 'Biologia',
            'observacoes': 'Muito boa!'
        }
        response = self.app.post('/professores', json=professor_data)
        professor_id = response.json['id']
        response = self.app.delete(f'/professores/{professor_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)

    # Teste 6: Adicionar aluno
    def test_006_add_aluno(self):
        aluno_data = {
            'nome': 'Joaquim',
            'idade': 18,
            'turma': 1, 
            'data_nasc': '2000-01-01',
            'nota_primeiro_sem': 8.5,
            'nota_segundo_sem': 9.5
        }
        response = self.app.post('/alunos', json=aluno_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('aluno_id', response.json) 
        self.assertEqual(response.json['nome'], 'Joaquim')

    # Teste 7: Buscar todos os alunos
    def test_007_get_alunos(self):
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    # Teste 8: Buscar aluno por ID
    def test_008_get_aluno(self):
        aluno_data = {
            'nome': 'Lucas',
            'idade': 20,
            'turma': 1,
            'data_nasc': '2001-05-10',
            'nota_primeiro_sem': 7.5,
            'nota_segundo_sem': 8.0
        }
        response = self.app.post('/alunos', json=aluno_data)
        aluno_id = response.json['aluno_id']  
        response = self.app.get(f'/alunos/{aluno_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Lucas')

    # Teste 9: Atualizar aluno
    def test_009_update_aluno(self):
        aluno_data = {
            'nome': 'Carlos Oliveira',
            'idade': 22,
            'turma': 1,
            'data_nasc': '1999-08-15',
            'nota_primeiro_sem': 9.0,
            'nota_segundo_sem': 8.5
        }
        response = self.app.post('/alunos', json=aluno_data)
        aluno_id = response.json['aluno_id']  
        
        update_data = {
            'nome': 'Carlos Oliveira Silva',
            'idade': 23,
            'turma': 2, 
            'data_nasc': '1999-08-15',
            'nota_primeiro_sem': 8.0,
            'nota_segundo_sem': 9.0
        }
        response = self.app.put(f'/alunos/{aluno_id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Carlos Oliveira Silva')

    # Teste 10: Deletar aluno
    def test_010_delete_aluno(self):
        aluno_data = {
            'nome': 'Maria',
            'idade': 19,
            'turma': 1,
            'data_nasc': '2001-03-25',
            'nota_primeiro_sem': 6.5,
            'nota_segundo_sem': 7.5
        }
        response = self.app.post('/alunos', json=aluno_data)
        aluno_id = response.json['aluno_id']  
        response = self.app.delete(f'/alunos/{aluno_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)

    # Teste 11: Adicionar turma
    def test_011_add_turma(self):
        turma_data = {
            'descricao': 'Turma A',
            'professor_id': 1,  
            'ativo': True
        }
        response = self.app.post('/turmas', json=turma_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('turma_id', response.json) 
        self.assertEqual(response.json['descricao'], 'Turma A')

    # Teste 12: Buscar todas as turmas
    def test_012_get_turmas(self):
        response = self.app.get('/turmas')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    # Teste 13: Buscar turma por ID
    def test_013_get_turma(self):
        turma_data = {
            'descricao': 'Turma B',
            'professor_id': 1,
            'ativo': True
        }
        response = self.app.post('/turmas', json=turma_data)
        turma_id = response.json['turma_id'] 
        response = self.app.get(f'/turmas/{turma_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['descricao'], 'Turma B')

    # Teste 14: Atualizar turma
    def test_014_update_turma(self):
        turma_data = {
            'descricao': 'Turma C',
            'professor_id': 2,
            'ativo': False
        }
        response = self.app.post('/turmas', json=turma_data)
        turma_id = response.json['turma_id'] 
        
        update_data = {
            'descricao': 'Turma C - Atualizada',
            'professor_id': 2,
            'ativo': True
        }
        response = self.app.put(f'/turmas/{turma_id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['descricao'], 'Turma C - Atualizada')

    # Teste 15: Deletar turma
    def test_015_delete_turma(self):
        turma_data = {
            'descricao': 'Turma D',
            'professor_id': 3,
            'ativo': True
        }
        response = self.app.post('/turmas', json=turma_data)
        turma_id = response.json['turma_id'] 
        response = self.app.delete(f'/turmas/{turma_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Turma excluída com sucesso!')

if __name__ == '__main__':
    unittest.main(verbosity=2)
