from django.shortcuts import render
from . import metrics

def home(request):

    product_metrics = metrics.get_product_metrics()

    context = {
        'product_metrics': product_metrics,
    }
    return render(request, 'home.html', context)








# product_metrics = {        
    #     'total_cost_price': 100000,
    #     'total_selling_price': 22000,
    #     'total_quantity': 1000,
    #     'total_profit': 3300000,
    # }