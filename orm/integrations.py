from .helpers import custom_query
from .models import Cliente, Produto, Pedido, PedidoProduto

SQL_1 = """
SELECT TO_NUMBER(FRN.CODFOR) AS ID,
       TRIM(INITCAP(FRN.NOMFOR)) AS RAZAO_SOCIAL,
       TRIM(INITCAP(FRN.APEFOR)) AS NOME_FANTASIA,
       FRN.TIPFOR AS TIPO,
       0 AS SALDO
  FROM E095FOR FRN
 WHERE EXISTS (
   SELECT 1
     FROM E420OCP OCP
    WHERE TO_CHAR(OCP.DATEMI, 'YYYY-MM') = '2018-04'
      AND OCP.CODFOR = FRN.CODFOR
      AND OCP.CODEMP = 3
 )
 ORDER BY 2
"""

SQL_2 = """
SELECT TO_NUMBER(PRO.CODPRO) AS ID,
       TRIM(INITCAP(PRO.DESPRO)) AS NOME,
       TRIM(INITCAP(PRO.CPLPRO)) AS DESCRICAO,
       0 AS SALDO,
       0 AS VALOR
  FROM E075PRO PRO
 WHERE PRO.CODEMP = 3
   AND EXISTS (
   SELECT 1
     FROM E420IPO IPO
    WHERE IPO.CODEMP = PRO.CODEMP
      AND IPO.CODPRO = PRO.CODPRO
      AND TO_CHAR(IPO.DATGER, 'YYYY-MM') = '2018-04'
 )
 ORDER BY 2
"""

SQL_3 = """
SELECT OCP.NUMOCP AS ID,
       OCP.CODFOR AS CLIENTE_ID,
       DECODE(OCP.SITOCP,
         9, 1,
         2, 2,
         3, 2,
         4, 4,
         5, 5,
         1
       ) AS SITUACAO,
       TRIM(INITCAP(OCP.OBSOCP)) AS OBSERVACAO,
       OCP.DATEMI AS DATA_INICIO,
       DECODE(OCP.SITOCP,
         2, OCP.DATGER,
         3, OCP.DATGER,
         NULL
       ) AS DATA_FECHADO,
       DECODE(OCP.SITOCP,
         4, OCP.DATFEC,
         NULL
       ) AS DATA_FINALIZADO,
       DECODE(OCP.SITOCP,
         5, OCP.DATEMI,
         NULL
       ) AS DATA_CANCELADO
       
  FROM E420OCP OCP
 WHERE TO_CHAR(OCP.DATEMI, 'YYYY-MM') = '2018-04'
   AND OCP.CODEMP = 3
   AND EXISTS (
     SELECT 1
       FROM E420IPO IPO
      WHERE IPO.CODEMP = OCP.CODEMP
        AND IPO.CODFIL = OCP.CODFIL
        AND IPO.NUMOCP = OCP.NUMOCP
   )
"""

SQL_4 = """
SELECT IPO.NUMOCP AS PEDIDO_ID,
       IPO.CODPRO AS PRODUTO_ID,
       IPO.QTDPED AS QUANTIDADE,
       IPO.PREUNI AS VALOR,
       TRIM(INITCAP(IPO.OBSIPO)) AS OBSERVACAO
  FROM E420IPO IPO
 WHERE IPO.CODEMP = 3
   AND TO_CHAR(IPO.DATGER, 'YYYY-MM') = '2018-04'
"""


class OrmIntegrador:

    def _clientes(self):
        return [Cliente(**c) for c in custom_query(SQL_1, [])]

    def _produtos(self):
        return [Produto(**p) for p in custom_query(SQL_2, [])]

    def _pedidos(self):
        return [Pedido(**p) for p in custom_query(SQL_3, [])]

    def _pedidos_produtos(self):
        return [PedidoProduto(**pp) for pp in custom_query(SQL_4)]

    def _limpar(self):
        PedidoProduto.objects.all().delete()
        Pedido.objects.all().delete()
        Cliente.objects.all().delete()
        Produto.objects.all().delete()

    def run(self, clean=False):
        if clean:
            self._limpar()
        Cliente.objects.bulk_create(self._clientes())
        Produto.objects.bulk_create(self._produtos())
        Pedido.objects.bulk_create(self._pedidos())
        PedidoProduto.objects.bulk_create(self._pedidos_produtos())
