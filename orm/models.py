from django.db import models


class Cliente(models.Model):
    TIPO = (
        ('F', 'Física'),
        ('J', 'Jurídica'),
    )
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO, default='F')
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        ordering = ('razao_social',)


class Produto(models.Model):
    TIPO = (
        ('P', 'Produto'),
        ('S', 'Serviço'),
    )
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    saldo = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Pedido(models.Model):
    SITUCAO = (
        (0, 'Iniciado'),
        (1, 'Confirmado'),
        (2, 'Fechado'),
        (3, 'Enviado'),
        (4, 'Finalizado'),
        (5, 'Cancelado'),
    )
    cliente = models.ForeignKey('orm.Cliente', on_delete=models.CASCADE)
    situacao = models.IntegerField(default=0, choices=SITUCAO)
    observacao = models.TextField(null=True, blank=True)
    data_inicio = models.DateField(auto_now_add=True)
    data_fechado = models.DateField(null=True, blank=True)
    data_enviado = models.DateField(null=True, blank=True)
    data_finalizado = models.DateField(null=True, blank=True)
    data_cancelado = models.DateField(null=True, blank=True)

    @property
    def total(self):
        return sum([i.total for i in self.pedidoproduto_set.all()])

    def __str__(self):
        return f'{self.pk}'


class PedidoProduto(models.Model):
    pedido = models.ForeignKey('orm.Pedido', on_delete=models.CASCADE)
    produto = models.ForeignKey('orm.Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    @property
    def total(self):
        return self.quantidade * self.valor

    acrescimos = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    descontos = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.pedido_id} / {self.produto.nome}'
