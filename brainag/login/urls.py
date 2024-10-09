from django.urls import include, path
from login.views import login_page, Autenticar

urlpatterns = [
    path('',  login_page),
    path('dologin', Autenticar ),
    # path('logout', Logout_Users, name='Logout'),

]