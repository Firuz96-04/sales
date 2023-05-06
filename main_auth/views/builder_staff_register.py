from rest_framework import mixins, generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from builders.models import Manager, SaleManager
from main_auth.models import CustomUser
from main_auth.permissions import BuilderManagerPermission
from main_auth.serializers import RegisterMangerSerializer, RegisterSerializer


class RegisterManagerApiView(mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterMangerSerializer
    permission_classes = (BuilderManagerPermission,)

    def create(self, request, *args, **kwargs):
        current_user = request.user
        user = RegisterMangerSerializer(data=request.data, context={'request': request})
        user.is_valid(raise_exception=True)
        user.save(builder_id=current_user.id)
        user_id = user.data['id']
        if user_id:
            manager = Manager.objects.get(user_id=user_id)
            manager.builder_id = current_user.id
            manager.save()
        return Response({'data': user.data})


class RegisterSaleManager(mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterMangerSerializer

    def post(self, request, *args, **kwargs):
        current_user = request.user
        user = RegisterMangerSerializer(data=request.data, context={'request': request})
        user.is_valid(raise_exception=True)
        user.save(builder_id=current_user.id)
        user_id = user.data['id']
        print(user_id, 'user_id')
        if user_id:
            sale = SaleManager.objects.get(user_id=user_id)
            sale.manager_id = current_user.id
            sale.save()
        return Response({'data': user.data})