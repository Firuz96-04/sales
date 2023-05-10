from rest_framework import mixins, generics, viewsets, status
from rest_framework.response import Response
from builders.serializers import (
    ClientNoticeApartmentSerializer,
)
from builders.permissions import OnlySaleManagerPermission
from builders.models import Client, SaleManager
from django_filters import rest_framework as filters
from builders.filters import ClientFilter


class ClientNoticeApartmentApiView(mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   generics.GenericAPIView):
    serializer_class = ClientNoticeApartmentSerializer
    permission_classes = (OnlySaleManagerPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter

    def get_queryset(self):
        sale_manager_id = self.request.user.id
        sale_manager = SaleManager.objects.get(user_id=sale_manager_id)
        manager_id = sale_manager.manager_id
        return Client.objects.filter(sale_manager__manager_id=manager_id).select_related('sale_manager', 'social_media')

    def get(self, request, *args, **kwargs):
        query = self.filter_queryset(self.get_queryset())
        serial = ClientNoticeApartmentSerializer(query, many=True)
        return Response({'data': serial.data})

    def post(self, request, *args, **kwargs):
        notice = ClientNoticeApartmentSerializer(data=request.data)
        notice.is_valid(raise_exception=True)
        notice.save()
        return Response({'data': notice.data})