from rest_framework import mixins, viewsets
from rest_framework.response import Response

from main_auth.models import CustomUser
from main_auth.serializers import RegisterSerializer


class RegisterView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = CustomUser.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        user = RegisterSerializer(data=request.data, context={'request': request})
        user.is_valid(raise_exception=True)
        user.save()
        print(request.user)
        # print(dir(user))
        # print('xello')
        # print(request.user)
        return Response(user.data)
