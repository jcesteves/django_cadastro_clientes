from django.shortcuts import render, redirect
from .models import Cliente
from .forms import Clienteform


def lista_cliente(request):
    cliente = Cliente.objects.all().order_by('-id')
    return render(request, 'clientes/cliente.html', {'cliente':cliente})

def add_cliente(request):
    form = Clienteform(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('list_cliente')
    
    return render(request, 'clientes/add_cliente.html', {'form':form})
