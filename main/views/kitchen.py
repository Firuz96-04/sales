from rest_framework import mixins, viewsets
from main.serializers import KitchenSerializer
from main.models import Kitchen
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class KitchenApiView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
