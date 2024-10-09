from rest_framework import serializers
from dashboard.models import Produtores, Fazendas, Culturas

class CulturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culturas
        fields = '__all__'

class FazendasSerializer(serializers.ModelSerializer):
    culturas = CulturasSerializer(many=True, read_only=True) 

    class Meta:
        model = Fazendas
        fields = '__all__'

    def validate_produtor(self, value):
        if not Produtores.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("O produtor não existe.")
        return value
    
class ProdutoresSerializer(serializers.ModelSerializer):
    fazendas = FazendasSerializer(many=True, read_only=True) 

    class Meta:
        model = Produtores
        fields = '__all__'

    def validate_cpfcnpj(self, value):

        if Produtores.objects.filter(cpfcnpj=value).exists():
            raise serializers.ValidationError("Já existe um produtor com este CPF ou CNPJ.")
        return value