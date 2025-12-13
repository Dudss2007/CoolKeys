from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='app'),
    path('add/<int:jogo_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('jogo/', views.jogo_detalhe_view, name='jogo_detalhe'),
]