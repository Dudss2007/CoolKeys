from django.shortcuts import render

def home_view(request):
    return render(
        request,
        'home.html'
    )
def carrinho_view(request):
    return render(
        request,
        'carrinho.html'
    )