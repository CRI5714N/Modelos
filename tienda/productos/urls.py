from django.urls import path
from.views import listar_clientes, listar_productos

urlppatterns = [
path('productos/', listar_productos)
 ]
