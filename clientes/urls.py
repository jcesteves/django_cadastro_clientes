from django.urls import path
from .views import lista_cliente, add_cliente


urlpatterns = [
    path('', lista_cliente, name='list_cliente'),
    path('add-cliente', add_cliente ),
]