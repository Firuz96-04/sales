from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from builders.models import ResidentComplex
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, JSONParser
from builders.permissions import OnlyBuilderPermission
from builders.serializers import ResidentComSerializer, ResidentManSerializerUpd
from main.serializers import (ElevatorSerializer, ParkingSerializer, KitchenSerializer, BuildingTypeSerializer,
                              DecorationSerializer, FacadeSerializer, HeatingSerializer)
from main.models import Elevator, Parking, Kitchen, Decoration, Facade, Heating, BuildingType


class ResidentComplexApiView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = ResidentComSerializer
    parser_classes = (MultiPartParser, JSONParser)
    permission_classes = (OnlyBuilderPermission,)

    def get_queryset(self):
        current = self.request.user
        return ResidentComplex.objects.prefetch_related('elevator', 'parking', 'building_type',
                                                        'decoration', 'facade', 'heating', 'kitchen'). \
            select_related('city', 'builder', 'building_class'). \
            filter(builder_id=current.id)

    def list(self, request, *args, **kwargs):
        complex = self.get_queryset()
        serial = ResidentComSerializer(complex, many=True)
        return Response({'data': serial.data})

    def create(self, request, *args, **kwargs):
        serial = ResidentComSerializer(data=request.data, context={"request": request})
        serial.is_valid(raise_exception=True)
        serial.save(builder_id=request.user.id)
        return Response({'data': serial.data}, status=status.HTTP_201_CREATED)


class ManagerComplexApiView(mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = ResidentComSerializer
    queryset = ResidentComplex.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        resident = ResidentComplex.objects.prefetch_related('elevator', 'parking', 'building_type',
                                                            'decoration', 'facade', 'heating', 'kitchen'). \
            select_related('city', 'builder', 'building_class') \
            .filter(manager_id=current_user.id)
        if resident:
            return resident.first()
        else:
            return []

    def list(self, request, *args, **kwargs):
        resident_query = self.get_queryset()
        if resident_query:
            complex_resident = ResidentComSerializer(self.get_queryset(), many=False)
            categories = {
                "elevator": ElevatorSerializer(Elevator.objects.all(), many=True).data,
                "parking": ParkingSerializer(Parking.objects.all(), many=True).data,
                "kitchen": KitchenSerializer(Kitchen.objects.all(), many=True).data,
                "decoration": DecorationSerializer(Decoration.objects.all(), many=True).data,
                "facade": FacadeSerializer(Facade.objects.all(), many=True).data,
                "heating": HeatingSerializer(Heating.objects.all(), many=True).data,
                "building_type": BuildingTypeSerializer(BuildingType.objects.all(), many=True).data,
            }
            return Response({'data': complex_resident.data, 'categories': categories})
        return Response({'data': dict(), 'categories': list(), 'message': 'manager does not connect with resident '
                                                                          'complex'})

    def put(self, request, *args, **kwargs):
        curr_user = request.user.id
        complex = ResidentComplex.objects.filter(manager_id=curr_user, manager__isnull=False)
        if complex.exists():
            serial = ResidentManSerializerUpd(complex.first(), data=request.data)
            serial.is_valid(raise_exception=True)
            serial.save()
            return Response({'data': serial.data})
        return Response({'error': 'manager not found'})
