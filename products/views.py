from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers
from categories.models import Category
from brands.models import Brand
from project_sge import metrics
from rest_framework import generics

class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product' # brands.view_brand = "nome do app . ação da permissão no caso visualização _ nome da model em minusculo"

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
        context['product_metrics'] = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context
    

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'
    
    

# API
class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
