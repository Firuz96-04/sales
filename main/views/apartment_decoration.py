from main.serializers import ApartmentDecorationSerializer
from rest_framework import mixins, viewsets
from main.models import ApartmentDecoration
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class ApartmentDecorationApiView(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    queryset = ApartmentDecoration.objects.all()
    serializer_class = ApartmentDecorationSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
