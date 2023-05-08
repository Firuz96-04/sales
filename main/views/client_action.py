from rest_framework import mixins, viewsets
from main.serializers import SaleManagerActionSerializer
from main.models import SaleManagerAction
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class SaleManagerActionApiView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    queryset = SaleManagerAction.objects.all()
    serializer_class = SaleManagerActionSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
