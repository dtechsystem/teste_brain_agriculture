from rest_framework import viewsets
from dashboard.models import Produtores, Fazendas, Culturas
from .serializers import ProdutoresSerializer, FazendasSerializer, CulturasSerializer, FazendasSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from django.db.models import Sum, Count

class ProdutoresViewSet(viewsets.ModelViewSet):
    queryset = Produtores.objects.all()
    serializer_class = ProdutoresSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)  # Lança ValidationError se não for válido
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorno correto
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:  # Captura qualquer outra exceção não prevista
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FazendasViewSet(viewsets.ModelViewSet):
    queryset = Fazendas.objects.all()
    serializer_class = FazendasSerializer

    def perform_create(self, serializer):
        produtor_id = self.request.data.get('produtor')
        if produtor_id is None:
            raise ValidationError({"detail": "O campo 'produtor' é obrigatório."})

        # Aqui já é garantido pela ForeignKey, mas você pode verificar novamente
        if not Produtores.objects.filter(id=produtor_id).exists():
            raise ValidationError({"detail": "O produtor não existe."})

        serializer.save()

class CulturasViewSet(viewsets.ModelViewSet):
    queryset = Culturas.objects.all()
    serializer_class = CulturasSerializer

    @action(detail=False, methods=['get'])
    def relatorio(self, request):

        relatorio_data = {

            'total_culturas': self.queryset.count(),
   
        }
        return Response(relatorio_data)
class DashboardDataView(APIView):
    def get(self, request):
        # Agregação por estado (soma das áreas)
        dados_por_estado = Fazendas.objects.values('estado').annotate(
            total_area=Sum('area_total'),
            area_agricultavel=Sum('area_agricultavel'),
            area_vegetacao=Sum('area_vegetacao')
        )

        # Agregação por cultura (quantidade de culturas plantadas)
        dados_por_cultura = Culturas.objects.values('cultura').annotate(
            total_fazendas=Count('fazenda')
        )

        # Agregação de uso do solo (soma das áreas)
        uso_do_solo = Fazendas.objects.aggregate(
            total_area=Sum('area_total'),
            area_agricultavel=Sum('area_agricultavel'),
            area_vegetacao=Sum('area_vegetacao')
        )

        # Formatar os dados para o dashboard
        data = {
            'dados_por_estado': list(dados_por_estado),
            'dados_por_cultura': list(dados_por_cultura),
            'uso_do_solo': uso_do_solo
        }

        return Response(data)