from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
def login_page(request):
    return render(request, 'login.html')

def Logout_Users(request):
    logout(request)
    return redirect('/')

@csrf_protect
def Autenticar(request):
    #return render(request,"forms.html")
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard',{'user':user})
        else:
            messages.error(request, ' Usuário ou senha inválidos!')
            return redirect('/')