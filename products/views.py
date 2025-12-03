# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from categories.models import Category
from brands.models import Brand

class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    # Filtra o nome da marca no campo de busca da pagina
    def get_queryset(self): # (sobrescrevendo a função queryset que antes pegava todos os campos da model product)
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        # Filtra por Título
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filtra por Número de Série
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        # Filtra por Categoria
        if category:
            queryset = queryset.filter(category__id=category)

        # Filtra por Marca
        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    
    # Método utilizado para passar mais objetos para o contexto (o campo context_object_name ja passa o Produto como contexto)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context
    

class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'

class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
