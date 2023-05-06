from rest_framework import mixins, viewsets
from main.serializers import HeatingSerializer
from main.models import Heating
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class HeatingApiView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Heating.objects.all()
    serializer_class = HeatingSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]