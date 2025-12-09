# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms
from project_sge import metrics

class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    # Filtra o produto no campo de busca da pagina
    def get_queryset(self): # (sobrescrevendo a função queryset que antes pegava todos os campos da model Brand)
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context
    

class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
