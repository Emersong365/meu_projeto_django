from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'app/lista.html', {'produtos': produtos})
from django.shortcuts import render

# Create your views here.
