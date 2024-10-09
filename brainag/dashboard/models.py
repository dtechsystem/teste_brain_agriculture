from django.db import models
from api.validators import validar_cpf, validar_cnpj
from django.core.exceptions import ValidationError

# Create your models here.
class Produtores(models.Model):
    id = models.AutoField(primary_key=True)
    cpfcnpj = models.CharField(null=True, blank=True)
    produtor = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'produtores'

    def clean(self):
        if self.cpfcnpj:
            cpfcnpj = self.cpfcnpj.replace(".", "").replace("-", "").replace("/", "")
            if len(cpfcnpj) == 11:  
                if not validar_cpf(cpfcnpj):
                    raise ValidationError("CPF inválido.")
            elif len(cpfcnpj) == 14:
                if not validar_cnpj(cpfcnpj):
                    raise ValidationError("CNPJ inválido.")
            else:
                raise ValidationError("CNPJ ou CPF deve ter 11 ou 14 dígitos.")

    def save(self, *args, **kwargs):
        self.clean()  # Chama o método de limpeza antes de salvar
        super().save(*args, **kwargs)

class Fazendas(models.Model):
    id = models.AutoField(primary_key=True)
    produtor = models.ForeignKey(Produtores, related_name='fazendas', on_delete=models.CASCADE)  # Adicionado related_name
    fazenda = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    cidade = models.CharField(null=True, blank=True)
    area_total = models.IntegerField(null=True, blank=True)
    area_agricultavel = models.IntegerField(null=True, blank=True)
    area_vegetacao = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'fazendas'

class Culturas(models.Model):
    id = models.AutoField(primary_key=True)
    cultura = models.CharField(null=True, blank=True)
    fazenda = models.ForeignKey(Fazendas, related_name='culturas', on_delete=models.CASCADE)  # Adicionado related_name
    
    class Meta:
        db_table = 'culturas'
