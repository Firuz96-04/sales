from rest_framework import mixins, viewsets
from main.serializers import FloorTypeSerializer
from main.models import FloorType
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class FloorTypeApiView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = FloorType.objects.all()
    serializer_class = FloorTypeSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]