from .models import Compra, ItemCompra, Categoria
from django.db.models import Sum

def carrinho_context(request): 
    total_itens_carrinho = 0
    
    # 1. Verifica se o usuário está autenticado
    if request.user.is_authenticated:
        try:
            # Busca o carrinho ativo (status='pendente') do usuário
            carrinho = Compra.objects.get(usuario=request.user, status='pendente')
            
            # 2. CALCULA O TOTAL DE QUANTIDADES 
            # Soma todas as colunas 'quantidade' na tabela ItemCompra relacionadas ao carrinho.
            soma = carrinho.itens.aggregate(total=Sum('quantidade'))
            
            # Pega o resultado da soma; se for None (carrinho vazio), usa 0.
            total_itens_carrinho = soma['total'] or 0
            
        except Compra.DoesNotExist:
            # Se não encontrou carrinho pendente, total é 0.
            pass
            
    # Retorna o dicionário de contexto.
    return {
        'total_itens_carrinho': total_itens_carrinho,
    }

def lista_categorias_view(request):
    # Isso torna a variável 'categorias' disponível em TODO o site
    return {request, {'categorias': Categoria.objects.all()}}