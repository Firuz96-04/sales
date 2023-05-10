from rest_framework import mixins, viewsets
from main.serializers import SocialMediaSerializer
from main.models import SocialMedia
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class SocialMediaApiView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
