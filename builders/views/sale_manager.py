from rest_framework import mixins, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from builders.serializers import (
    ClientNoticeApartmentSerializer,
)
from builders.models import Client


class ClientNoticeApartmentApiView(mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientNoticeApartmentSerializer

    def get(self, request, *args, **kwargs):
        serial = ClientNoticeApartmentSerializer(self.get_queryset(), many=True)
        return Response({'data': serial.data})

    def post(self, request, *args, **kwargs):

        return Response({'data': 'post'})