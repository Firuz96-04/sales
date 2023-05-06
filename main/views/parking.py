from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from main.serializers import ParkingSerializer
from main.models import Parking
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class ParkingApiView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
