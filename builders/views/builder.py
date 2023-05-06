import os

from rest_framework import mixins, generics, viewsets, status
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from builders.models import (Builder, ResidentComplex)
from builders.permissions import OnlyBuilderPermission
from builders.serializers import *

from main_auth.models import CustomUser


class BuilderApiView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Builder.objects.all()
    # serializer_class = BuilderSerializer
    parser_classes = (FormParser, JSONParser)

    def list(self, request, *args, **kwargs):
        build = BuilderSerializer(self.get_queryset(), many=True)
        return Response({'data': build.data})

    # def create(self, request, *args, **kwargs):
    #     build = BuilderSerializer(data=request.data)
    #     build.is_valid(raise_exception=True)
    #     build.save()
    #     return Response({'message': build.data})

    @action(detail=False, methods=['put'])
    def manager_connect(self, request):
        complex_id = request.query_params['id']
        resident_comp = ResidentComplex.objects.get(id=complex_id)
        serial = ManagerComplexConnectSerializer(resident_comp, data=request.data,
                                                 context={'builder': self.request.user.id})
        serial.is_valid(raise_exception=True)
        serial.save()
        # print(resident_comp)
        return Response({'message': serial.data})


class BuilderVerifyView(mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    queryset = Builder.objects.order_by('-user_id')
    parser_classes = (MultiPartParser, JSONParser)
    # serializer_class = BuilderVerifySerializer

    # def get(self, request, *args, **kwargs):
    #     # builder = BuilderVerifySerializer(self.get_queryset(), many=True)
    #
    #     return Response({'data': builder.data})

    def put(self, request, *args, **kwargs):
        current_user = request.user.id
        builder = Builder.objects.get(user_id=current_user)
        verify = BuilderVerifySerializer(builder, data=request.data)
        verify.is_valid(raise_exception=True)
        verify.save()
        custom = CustomUser.objects.get(pk=current_user)
        custom.status_id = 3
        custom.save()
        # UserStatus.objects.get(pk=3)
        return Response({'data': verify.data, 'success': 'You have successfully submitted, please wait for a response'})


class BuilderApiViewUpd(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer

    def put(self, request, *args, **kwargs):
        id = kwargs['pk']
        # print(request.FILES, 'files')
        build = Builder.objects.get(pk=id)
        serial = BuilderSerializer(build, data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response({'data': serial.data})

    def delete(self, request, *args, **kwargs):
        id = kwargs['pk']
        build = Builder.objects.get(pk=id)
        image = build.image_logo
        if os.path.exists(image.path):
            build.delete()
            os.remove(image.path)
            parent_folder = os.path.dirname(image.path)
            if not os.listdir(parent_folder):
                os.rmdir(parent_folder)
            return Response({'file': 'exist'})
        return Response({'file': 'not exists'})


class ComplexManagerConnectApi(mixins.ListModelMixin,
                               mixins.UpdateModelMixin,
                               viewsets.GenericViewSet):
    serializer_class = ComplexManagerSerializer
    permission_classes = [OnlyBuilderPermission,]

    def get_queryset(self):
        return ResidentComplex.objects.filter(builder_id=self.request.user.id)

    def put(self, request, *args, **kwargs):
        complex_id = self.request.query_params.get('id')
        print(complex_id)
        resident_complex = ResidentComplex.objects.get(id=complex_id)
        serial = ComplexManagerSerializer(resident_complex, data=request.data, context={'id': complex_id})
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response({'data': serial.data})