from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='app'),
    path('carrinho/', views.carrinho_view, name='carrinho'),

]