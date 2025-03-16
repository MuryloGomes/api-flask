import unittest
from app import app
from modelos import professores, alunos, turmas, Professor, Aluno, Turma
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        professores.clear()
        alunos.clear()
        turmas.clear()

    def test_get_professores(self):
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])
    def test_add_professor(self):
        professor_data = {
            'nome': 'John Doe',
            'idade': 30,
            'disciplina': 'Matemática',
            'observacoes': 'Muito bom!'
        }
        response = self.app.post('/professores', json=professor_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual('id', response.json)
        self.assertEqual(response.json['nome'], 'John Doe')
        
    def test_get_professor(self):
        professor_data = {
            'nome': 'Maria',
            'idade': 25,
            'disciplina': 'Fisica',
            'observacoes': 'Excelente!'
        }
        response = self.app.post('/professores', json=professor_data)
        professor_id = response.json['id']
        response = self.app.get(f'/professores/{professor_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], professor_id)
        
    def test_delete_professor(self):
        professor_data = {
            'nome': 'Maria',
            'idade': 25,
            'disciplina': 'Fisica',
            'observacoes': 'Excelente!'
        }
        response = self.app.post('/professores', json=professor_data)
        professor_id = response.json['id']
        response = self.app.delete(f'/professores/{professor_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Professor deletado com sucesso')
        
    def test_update_professor(self):
        professor_data = {
            'nome': 'Fernanda',
            'idade': 45,
            'disciplina': 'Biologia',
            'observacoes': 'Muito boa'
        }
        response = self.app.post('/professores', json=professor_data)
        professor_id = response.json['id']
        
        update_data = {
            'nome': 'Fernanda',
            'idade': 45,
            'disciplina': 'Biologia',
            'observacoes': 'Muito boa'
        }
        response = self.app.put(f'/professores/{professor_id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Fernanda Silva')
        
    def test_add_alunos(self):
        aluno_data = {
            'nome': 'Joaquim',
            'idade': 18,
            'turma_id': 1,
            'data_nascimento': '2000-01-01',
            'nota_primeiro_semestre': 8.5,
            'nota_segundo_semestre': 9.5
        }
        response = self.app.post('/alunos', json=aluno_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual('id', response.json)
        self.assertEqual(response.json['nome'], 'Joaquim')
        
    if __name__ == '__main__':
        unittest.main()