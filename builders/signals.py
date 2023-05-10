from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Apartment, ApartmentPrice, Client


@receiver(pre_save, sender=Apartment)
def edit_apartment_price(sender, instance, **kwargs):
    try:
        apartment = Apartment.objects.get(pk=instance.id)
    except sender.DoesNotExist:
        pass
    else:
        if apartment.price != instance.price:
            ApartmentPrice.objects.create(price=instance.price, apartment_id=instance.id)


@receiver(post_save, sender=Apartment)
def add_apartment_price(sender, instance, created, **kwargs):
    if created:
        print('created method')
        ApartmentPrice.objects.create(price=instance.price, apartment_id=instance.id)


@receiver(post_save, sender=Client)
def add_apartment_status(sender, instance, created, **kwargs):
    if created:
        print(instance.apartment_id)
        apartment = Apartment.objects.get(pk=instance.apartment_id)
        apartment.status_id = 3
        apartment.save()
        print('client is add')