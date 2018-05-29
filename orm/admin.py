from django.contrib import admin
from .models import *


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'razao_social',
        'nome_fantasia',
        'tipo',
        'saldo',
    ]
    list_filter = ('tipo', 'saldo')
    search_fields = ('razao_social', 'nome_fantasia')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'descricao',
        'saldo',
        'valor',
    ]
    list_filter = ('valor', 'saldo')
    search_fields = ('nome', 'descricao')


class PedidoProdutoInLine(admin.TabularInline):
    model = PedidoProduto


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cliente',
        'situacao',
        'observacao',
        'data_inicio',
        'total'
    ]
    list_filter = ('data_inicio', 'situacao')
    search_fields = ('cliente__nome_fantasia', 'cliente__razao_social', 'observacao')

    inlines = [
        PedidoProdutoInLine
    ]
