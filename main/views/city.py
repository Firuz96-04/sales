from rest_framework import mixins, generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from main.serializers import *
from main_auth import permissions


class CityApiView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = City.objects.select_related('region').order_by('-id')
    serializer_class = CitySerializer
    permission_classes = (permissions.MyAdminUser,)

    def list(self, request, *args, **kwargs):
        city = City.objects.select_related('region').order_by('-id')
        city_serial = CitySerializer(city, many=True)
        return Response({'data': city_serial.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        city = CitySerializer(data=request.data)
        city.is_valid(raise_exception=True)
        city.save()
        return Response({'data': city.data}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        city_id = request.query_params.get('id')
        city = City.objects.filter(id=city_id).first()
        if city is not None:
            city_serial = CityUpdSerializer(city, data=request.data)
            city_serial.is_valid(raise_exception=True)
            city_serial.save()
            return Response(city_serial.data, status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError({'error': f'{city_id} id not found'})

    def delete(self, request, *args, **kwargs):
        city_id = request.query_params.get('id')
        try:
            city = City.objects.get(id=city_id)
            city.delete()
        except Exception as e:
            raise serializers.ValidationError({'error': 'you cant delete it'})
        else:
            return Response({'data': city.name})

    @action(detail=False, methods=['get'])
    def info(self, request, pk=None):
        return Response({'message': 'wqeqw'})
