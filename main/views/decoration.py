from rest_framework import mixins, viewsets, status
from main.serializers import DecorationSerializer
from main.models import Decoration
from main.permissions import CategoryOnlyAdmin
from rest_framework.permissions import IsAuthenticated


class DecorationApiView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Decoration.objects.all()
    serializer_class = DecorationSerializer

    # permission_classes = (permissions.CategoryOnlyAdmin,)

    def get_permissions(self):
        if self.action in ('list',):
            return [IsAuthenticated()]
        elif self.action in ('list', 'update', 'create', 'destroy'):
            return [CategoryOnlyAdmin()]
        else:
            return [IsAuthenticated()]
