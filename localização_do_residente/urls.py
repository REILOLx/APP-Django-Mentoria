from django.urls import path
from .views import EnderecoAPI, EnderecoDetailAPI, ResidenteAPI, ResidenteDetailAPI

urlpatterns = [
    path('endereco/', EnderecoAPI.as_view(), name='endereco_all'),
    path('endereco/<int:id_endereco>/', EnderecoDetailAPI.as_view(), name='endereco_details'),
    path('residente/', ResidenteAPI.as_view(), name='residente_all'),
    path('residente/<int:id_residente>/', ResidenteDetailAPI.as_view(), name='residente_details'),
]
