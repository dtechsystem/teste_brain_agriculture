from django.urls import include, path
from .views import Dashboard, Municipios, Cadastrar_Produtor, View_Produtor, Editar_Produtor, Remover_Fazenda, Remover_Cultura, Editar_Dados_Produtor, Cadastrar_Fazenda,View_Culturas,Cadastrar_Culturas, Editar_Fazenda,Remover_Produtor

urlpatterns = [
    path('dashboard',  Dashboard),
    path('ajax/buscar-municipios',Municipios),
    path('cadastrar-produtor',  Cadastrar_Produtor),
    path('cadastrar-fazenda',  Cadastrar_Fazenda),
    path('cadastrar-culturas',  Cadastrar_Culturas),
    path('view-produtor/<int:id>',  View_Produtor),
    path('view-culturas/<int:id>',  View_Culturas),
    path('editar/<int:id>',  Editar_Produtor),
    path('editar-produtor',  Editar_Dados_Produtor),
    path('editar-fazenda',  Editar_Fazenda),
    path('remover-fazenda',  Remover_Fazenda),
    path('remover-cultura',  Remover_Cultura),
    path('deletar-produtor',  Remover_Produtor),



]