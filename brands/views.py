# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms

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
    

class BrandCreateView(CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'

