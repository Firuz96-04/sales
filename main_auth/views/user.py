from rest_framework import mixins, generics
from rest_framework.response import Response

from main_auth.models import CustomUser
from main_auth.serializers import UserSerializer


class UserApiView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = UserSerializer(self.get_queryset(), many=True)
        return Response({'data': user.data})
