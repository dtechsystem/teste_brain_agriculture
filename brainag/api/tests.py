from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from dashboard.models import Produtores, Fazendas, Culturas

class APITestCase(TestCase):
    
    def setUp(self):
  
        self.produtor = Produtores.objects.create(
            cpfcnpj="05798883043", produtor="Produtor 1"
        )
        self.fazenda1 = Fazendas.objects.create(
            produtor=self.produtor,
            fazenda="Fazenda 1",
            estado="GO",
            cidade="Cidade 1",
            area_total=500,
            area_agricultavel=300,
            area_vegetacao=200
        )
        self.fazenda2 = Fazendas.objects.create(
            produtor=self.produtor,
            fazenda="Fazenda 2",
            estado="SP",
            cidade="Cidade 2",
            area_total=1000,
            area_agricultavel=800,
            area_vegetacao=200
        )
        self.cultura1 = Culturas.objects.create(
            fazenda=self.fazenda1, cultura="Soja"
        )
        self.cultura2 = Culturas.objects.create(
            fazenda=self.fazenda2, cultura="Milho"
        )


        self.client = APIClient()

    def test_dashboard_data(self):

        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        data = response.json()
        
 
        self.assertIn('dados_por_estado', data)


        dados_por_estado = sorted(data['dados_por_estado'], key=lambda x: x['estado'])

        self.assertEqual(dados_por_estado[0]['estado'], 'GO')
        self.assertEqual(dados_por_estado[1]['estado'], 'SP')


        self.assertIn('dados_por_cultura', data)
        

        dados_por_cultura = sorted(data['dados_por_cultura'], key=lambda x: x['cultura'])

        self.assertEqual(dados_por_cultura[0]['cultura'], 'Milho')
        self.assertEqual(dados_por_cultura[1]['cultura'], 'Soja')


        self.assertIn('uso_do_solo', data)
        self.assertEqual(data['uso_do_solo']['total_area'], 1500)  # 500 + 1000

    def test_create_produtor(self):

        payload = {
            "cpfcnpj": "54854697016",
            "produtor": "Produtor 2"
        }
        response = self.client.post('/api/produtores/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_fazenda(self):

        payload = {
            "produtor": self.produtor.id,
            "fazenda": "Fazenda 3",
            "estado": "MG",
            "cidade": "Cidade 3",
            "area_total": 700,
            "area_agricultavel": 500,
            "area_vegetacao": 200
        }
        response = self.client.post('/api/fazendas/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_cultura(self):
       
        payload = {
            "fazenda": self.fazenda1.id,
            "cultura": "Algodão"
        }
        response = self.client.post('/api/culturas/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_produtor(self):
    
        response = self.client.delete(f'/api/produtores/{self.produtor.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
