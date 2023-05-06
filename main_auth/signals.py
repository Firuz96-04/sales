from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user
from .models import CustomUser
from builders.models import Builder, Manager, SaleManager
import jwt


@receiver(post_save, sender=CustomUser)
def creat_user_check(sender, instance, created, **kwargs):
    # print(dir(instance), instance.role, 'instance')
    # print(instance)

    # jwt_token = kwargs['request'].META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    #
    # # Decode the token to get the user ID
    # decoded_token = jwt.decode(jwt_token, 'secret_key', algorithms=['HS256'])
    # user_id = decoded_token['user_id']
    # print(user_id, 'instances')
    if created:
        if instance.role.name == 'builder':
            Builder.objects.create(
                user=instance)
        if instance.role.name == 'manager':
            Manager.objects.create(user=instance)

        if instance.role.name == 'salemanager':
            SaleManager.objects.create(user=instance)
    else:
        pass
        # print('not created')