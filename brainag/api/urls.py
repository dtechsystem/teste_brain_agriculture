from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoresViewSet, FazendasViewSet, CulturasViewSet
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DashboardDataView

router = DefaultRouter()
router.register(r'produtores', ProdutoresViewSet)
router.register(r'fazendas', FazendasViewSet)
router.register(r'culturas', CulturasViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/dashboard/', DashboardDataView.as_view(), name='dashboard_data'),

]
