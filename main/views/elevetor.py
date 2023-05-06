from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from main.serializers import ElevatorSerializer
from main.models import Elevator
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import AllowAny, IsAuthenticated


class ElevatorApiView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]