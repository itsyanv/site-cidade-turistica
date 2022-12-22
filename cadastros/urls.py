from django.urls import path
from .views import EstadoCreate, CidadeCreate, PontoCreate
from .views import EstadoUpdate, CidadeUpdate, PontoUpdate
from .views import EstadoDelete, CidadeDelete, PontoDelete
from .views import EstadoList, CidadeList, PontoList

urlpatterns = [    
    ### CREATE VIEW ###
    path('Cadastro-Estado/', EstadoCreate.as_view(), name='cadastro-estado'),
    path('Cadastro-Cidade/', CidadeCreate.as_view(), name='cadastro-cidade'),
    path('Cadastro-Ponto/', PontoCreate.as_view(), name='cadastro-ponto'),

    ### UPDATE VIEW ###
    path('Editar-Estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('Editar-Cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('Editar-Ponto/<int:pk>/', PontoUpdate.as_view(), name='editar-ponto'),

    ### DELETE VIEW ###
    path('Excluir-Estado/<int:pk>/', EstadoDelete.as_view(), name='excluir-estado'),
    path('Excluir-Cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('Excluir-Ponto/<int:pk>/', PontoDelete.as_view(), name='excluir-ponto'),

    ### LIST VIEW ###
    path('Estados/', EstadoList.as_view(), name='listar-estados'),
    path('Cidades/', CidadeList.as_view(), name='listar-cidades'),
    path('Pontos/', PontoList.as_view(), name='listar-pontos'),
]