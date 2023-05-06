from rest_framework import mixins, viewsets
from main.serializers import FacadeSerializer
from main.models import Facade
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class FacadeApiView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Facade.objects.all()
    serializer_class = FacadeSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
