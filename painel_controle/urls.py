from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('jogos/criar/', views.criar_jogo_view, name='criar_jogo'),
    path('jogo/editar/<int:jogo_id>/', views.editar_jogo, name='editar_jogo'),
    path('categorias/', views.gerenciar_categorias, name='gerenciar_categorias'), # Nome usado nos redirects das views
    path('categorias/edit/<int:cat_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/delete/<int:cat_id>/', views.deletar_categoria, name='deletar_categoria'),
    path('usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('usuarios/grupo/<int:user_id>/', views.alterar_grupo_usuario, name='alterar_grupo'),
    path('usuarios/deletar/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
 ]