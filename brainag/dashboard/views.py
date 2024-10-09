from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.db import transaction
from .models import Produtores,Culturas,Fazendas
from django.db.models import Count,Sum
from django.http import JsonResponse
import plotly.express as px

# Create your views here.
def Dashboard(request):
    produtores_com_fazendas = Produtores.objects.annotate(
        quantidade_fazendas=Count('fazendas'),
        area_total=Sum('fazendas__area_total'),  
        area_agricultavel=Sum('fazendas__area_agricultavel') 
    )

    total_fazendas = Fazendas.objects.all().count()
    total_area = Fazendas.objects.aggregate(Sum('area_total'))['area_total__sum']

    fazendas_por_estado = Fazendas.objects.values('estado').annotate(total=Count('id'))
    
    # Dados para gráfico por cultura
    culturas_por_fazenda = Culturas.objects.values('cultura').annotate(total=Count('id'))

    # Dados para gráfico por uso de solo
    uso_solo = Fazendas.objects.aggregate(
        total_agricultavel=Sum('area_agricultavel'),
        total_vegetacao=Sum('area_vegetacao')
    )

    # Gráfico por estado
    estados = [item['estado'] for item in fazendas_por_estado]
    total_fazendas_estado = [item['total'] for item in fazendas_por_estado]
    
    # Gráfico por cultura
    culturas = [item['cultura'] for item in culturas_por_fazenda]
    total_culturas = [item['total'] for item in culturas_por_fazenda]
    
    # Gráfico por uso de solo
    uso_solo_data = [uso_solo['total_agricultavel'], uso_solo['total_vegetacao']]
    uso_solo_labels = ['Área Agricultável', 'Área de Vegetação']

    # Passar os gráficos e dados para o template
    context = {
        'total_area': total_area,
        'estados': estados,
        'total_fazendas_estado': total_fazendas_estado,
        'culturas_labels': culturas,
        'total_culturas': total_culturas,
        'uso_solo_labels': uso_solo_labels,
        'uso_solo_data': uso_solo_data,
    }
    return render(request,'dashboard.html',{'produtores_com_fazendas':produtores_com_fazendas,'total_fazendas':total_fazendas,'total_area':total_area, **context})

@login_required(login_url='/')
def Municipios(request):
    
    estado = request.GET.get('estado')
    requisicao = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/distritos?orderBy=nome')
    requisicao_json = requisicao.json()
    return render(request, 'ajax/ajax_municipios.html', {'dados': requisicao_json})

@login_required(login_url='/')
def Cadastrar_Produtor(request):
    #Verifica se o cpf já está cadastrado
    cpf_is_registered = Produtores.objects.filter(cpfcnpj = request.POST.get('dados[cpfCnpj]')).exists()
    print(request.POST)

    cpf_cnpj = request.POST.get('dados[cpfCnpj]')
    nome_produtor = request.POST.get('dados[nomeProdutor]')
    nome_fazenda = request.POST.get('dados[nomeFazenda]')
    estado = request.POST.get('dados[estado]')
    municipio = request.POST.get('dados[cidade]')
    area_total = request.POST.get('dados[areaTotal]')
    area_agricultura = request.POST.get('dados[areaAgricultavel]')
    area_vegetacao = request.POST.get('dados[areaVegetacao]')
    culturas = request.POST.getlist('dados[culturas][]')
    
    #Se não tiver cadastro segue o bloco abaixo
    if cpf_is_registered == True:
        produtor = Produtores.objects.filter(cpfcnpj = request.POST.get('dados[cpfCnpj]')).first()
        fazenda = Fazendas.objects.create(
            produtor = produtor,
            fazenda = nome_fazenda,
            estado = estado,
            cidade = municipio,
            area_total = area_total,
            area_agricultavel = area_agricultura,
            area_vegetacao = area_vegetacao
        )

        #Cadastrar Culturas
        for cultura in culturas:
            Culturas.objects.create(
                fazenda = fazenda,
                cultura = cultura
            )
    else:
       

        #Cadastrar Produtor
        with transaction.atomic():
            produtor = Produtores.objects.create(
                cpfcnpj = cpf_cnpj,
                produtor = nome_produtor,
            
            )

            #Cadastrar Fazendas
            fazenda = Fazendas.objects.create(
                produtor = produtor,
                fazenda = nome_fazenda,
                estado = estado,
                cidade = municipio,
                area_total = area_total,
                area_agricultavel = area_agricultura,
                area_vegetacao = area_vegetacao
            )

            #Cadastrar Culturas
            for cultura in culturas:
                Culturas.objects.create(
                    fazenda = fazenda,
                    cultura = cultura
                )

        
        

    return render(request, 'dashboard.html')

@login_required(login_url='/')
def Cadastrar_Culturas(request):
    print(request.POST)
    culturas = request.POST.getlist('culturas[]')
    fazenda_id = request.POST.get('fazenda_id')
    print(fazenda_id)
    #Apaga todas as culturas da fazenda
    Culturas.objects.filter(fazenda_id = fazenda_id).delete()
    for cultura in culturas:
        Culturas.objects.create(
            fazenda_id = fazenda_id,
            cultura = cultura
        )
    return JsonResponse({'message': 'Success'})

@login_required(login_url='/')
def Cadastrar_Fazenda(request):
    #Verifica se o cpf já está cadastrado
 
    nome_fazenda = request.POST.get('dados[nomeFazenda]')
    estado = request.POST.get('dados[estado]')
    municipio = request.POST.get('dados[cidade]')
    area_total = request.POST.get('dados[areaTotal]')
    area_agricultura = request.POST.get('dados[areaAgricultavel]')
    area_vegetacao = request.POST.get('dados[areaVegetacao]')
    culturas = request.POST.getlist('dados[culturas][]')
    produtor_id = request.POST.get('dados[produtorId]')
    print('produtor id = ', produtor_id)
    with transaction.atomic():
        try:
            produtor = Produtores.objects.filter(id = produtor_id).first()
            fazenda = Fazendas.objects.create(
                produtor = produtor,
                fazenda = nome_fazenda,
                estado = estado,
                cidade = municipio,
                area_total = area_total,
                area_agricultavel = area_agricultura,
                area_vegetacao = area_vegetacao
            )

            #Cadastrar Culturas
            for cultura in culturas:
                Culturas.objects.create(
                    fazenda = fazenda,
                    cultura = cultura
                )
        except:
            return JsonResponse({'message': 'Error'})
        
    

        
        

    return render(request, 'dashboard.html')

@login_required(login_url='/')
def View_Produtor(request, id):
    produtor = Produtores.objects.filter(id=id).first()

    fazendas = Fazendas.objects.filter(produtor=produtor)
    culturas = Culturas.objects.filter(fazenda__in=fazendas)


    fazendas_por_estado = fazendas.values('estado').annotate(total=Count('id'))

    culturas_por_fazenda = culturas.values('cultura').annotate(total=Count('id'))

    uso_solo = fazendas.aggregate(
        total_agricultavel=Sum('area_agricultavel'),
        total_vegetacao=Sum('area_vegetacao')
    )

    estados = [item['estado'] for item in fazendas_por_estado]
    total_fazendas_estado = [item['total'] for item in fazendas_por_estado]

    culturas_labels = [item['cultura'] for item in culturas_por_fazenda]
    total_culturas = [item['total'] for item in culturas_por_fazenda]

    uso_solo_labels = ['Área Agricultável', 'Área de Vegetação']
    uso_solo_data = [uso_solo['total_agricultavel'], uso_solo['total_vegetacao']]

    context = {
        'estados': estados,
        'total_fazendas_estado': total_fazendas_estado,
        'culturas_labels': culturas_labels,
        'total_culturas': total_culturas,
        'uso_solo_labels': uso_solo_labels,
        'uso_solo_data': uso_solo_data,
    }
    
    return render(request, 'ajax/modal_view_user.html', {'produtor':produtor, 'fazendas':fazendas, 'culturas':culturas,**context})

@login_required(login_url='/')
def View_Culturas(request, id):
    #Obter dados do produtor
    fazenda_id = id
   

    culturas = Culturas.objects.filter(fazenda_id = fazenda_id).values()
    culturas_selected = []
    for cultura in culturas:
        culturas_selected.append(cultura['cultura'])

    
    return render(request, 'ajax/ajax_modal_culturas.html', {'culturas':culturas_selected})

@login_required(login_url='/')
def Editar_Produtor(request, id):
    #Obter dados do produtor
    id_produtor = id
    print(id)
    produtor = Produtores.objects.filter(id = id_produtor).first()
    
    #Obter dados das fazendas e suas culturas
    fazendas = Fazendas.objects.filter(produtor = produtor)
    culturas = Culturas.objects.filter(fazenda__in = fazendas)

    return render(request, 'editar-produtor.html', {'produtor':produtor, 'fazendas':fazendas, 'culturas':culturas})

@login_required(login_url='/')
def Editar_Fazenda(request):
    fazenda_id = request.POST.get('dados[fazendaId]')
    nome_fazenda = request.POST.get('dados[nomeFazenda]')
    area_total = request.POST.get('dados[areaTotal]')
    area_agricultura = request.POST.get('dados[areaAgricultavel]')
    area_vegetacao = request.POST.get('dados[areaVegetacao]')

    Fazendas.objects.filter(id = fazenda_id).update(
        fazenda = nome_fazenda,
        area_total = area_total,
        area_agricultavel = area_agricultura,
        area_vegetacao = area_vegetacao
    )


    return JsonResponse({'message': 'Success'})

@login_required(login_url='/')
def Editar_Dados_Produtor(request):
    #Obter dados do produtor
    id_produtor = request.POST.get('produtor_id')
    produtor = Produtores.objects.get(id = id_produtor)
    produtor.cpfcnpj = request.POST.get('cpfcnpj')
    produtor.produtor = request.POST.get('nome_produtor')
    produtor.save()
        
    return JsonResponse({'message': 'Success'})

@login_required(login_url='/')
def Remover_Fazenda(request):
    fazenda_id = request.POST.get('fazendaId')

    Fazendas.objects.filter(id = fazenda_id).delete()
    return JsonResponse({'message': 'Success'})

@login_required(login_url='/')
def Remover_Cultura(request):
    cultura_id = request.POST.get('culturaId')

    Culturas.objects.filter(id = cultura_id).delete()
    return JsonResponse({'message': 'Success'})

@login_required(login_url='/')
def Remover_Produtor(request):
    produtor_id = request.POST.get('id')

    Produtores.objects.filter(id = produtor_id).delete()
    return JsonResponse({'message': 'Success'})