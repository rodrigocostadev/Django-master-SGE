from products.models import Product
from django.utils.formats import number_format
from outflows.models import Outflow
from django.db.models import Sum

# Retorna as metricas de produto para mostrar no dashboard
def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum( product.cost_price * product.quantity for product in products )
    total_selling_price = sum( product.selling_price * product.quantity for product in products )
    total_quantity = sum( product.quantity for product in products )
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True), # o force_grouping é pra não agrupar as casas decimais
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(  # O método .aggregate() do Django executa uma operação de agregação no banco de dados e retorna um dicionário com o resultado.
        total_products_sold=Sum('quantity')
    )['total_products_sold'] or 0              # ['total_products_sold'] é o acesso ao valor da chave do dicionario, se não tiver resultado passa a ter valor 0
    total_sales_value= sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all() )
    total_sales_cost= sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all() )
    total_sales_profit= total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_products_sold,
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )

