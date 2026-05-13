from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflow
from services.notify import Notify
from datetime import datetime

@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()
            

@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, **kwargs):
    notify = Notify()
    
    data={
        "event_type": "create_outflow", # (Boa Prática) chave para identificar o tipo de evento
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # (Boa Prática) timestamp do evento
        "product": instance.product.title,
        "product_cost_price": float(instance.product.cost_price), # (Boa Prática) preço do produto convertido para string para evitar problemas de serialização
        "product_selling_price": float(instance.product.selling_price), # (Boa Prática) preço do produto convertido para string para evitar problemas de serialização
        "quantity": instance.quantity,
        "description": instance.description,
    }
    
    notify.send_order_event(data)
    print("Printou dados para o webhook")