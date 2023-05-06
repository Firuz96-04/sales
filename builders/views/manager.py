from rest_framework import mixins, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from builders.serializers import (
    ManagerSerializer,
)
from builders.models import Manager


class ManagerApiView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Manager.objects.select_related('user').order_by('user_id')
    serializer_class = ManagerSerializer

    def list(self, request, *args, **kwargs):
        manager = ManagerSerializer(self.get_queryset(), many=True)
        return Response({'data': manager.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def complex_info(self, request):
        return Response({'message': 'Info'})
