from rest_framework import mixins, viewsets, status
from main.serializers import BuildingTypeSerializer
from main.models import BuildingType
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class BuildingTypeApiView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = BuildingType.objects.all()
    serializer_class = BuildingTypeSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
