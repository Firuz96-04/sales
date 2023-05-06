from rest_framework import mixins, generics, status
from rest_framework.response import Response
from main.serializers import *


class RegionApiView(mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Region.objects.order_by('-id')
    serializer_class = RegionSerializer
    # permission_classes = (permissions.MyAdminUser,)

    def get(self, request, *args, **kwargs):
        region_serial = RegionSerializer(self.get_queryset(), many=True)
        return Response({'data': region_serial.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        region = RegionSerializer(data=request.data)
        region.is_valid(raise_exception=True)
        region.save()
        return Response({'data': region.data}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        region_id = request.query_params['id']
        region = Region.objects.filter(id=region_id).first()
        if region is not None:
            region_serial = RegionSerializer(region, data=request.data)
            region_serial.is_valid(raise_exception=True)
            region_serial.save()
            return Response(region_serial.data, status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError({'error': f'{region_id} id not found'})

    def delete(self, request, *args, **kwargs):
        region_id = request.query_params['id']
        try:
            region = Region.objects.get(id=region_id)
            region.delete()
        except Exception as e:
            raise serializers.ValidationError({'error': 'you cant delete it'})
        else:
            return Response({'data': region.name})


class RegionListApiView(generics.ListAPIView):
    queryset = Region.objects.prefetch_related('city_set')
    serializer_class = RegionListSerializer
    # permission_classes = (permissions.MyAdminUser,)
