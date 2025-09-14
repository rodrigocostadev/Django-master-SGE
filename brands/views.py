# from django.shortcuts import render
from django.views.generic import ListView
from . import models

class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    # Filtra o nome da marca no campo de busca da pagina
    def get_queryset(self): # (sobrescrevendo a função queryset que antes pegava todos os campos da model Brand)
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
