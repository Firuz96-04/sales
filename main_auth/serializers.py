from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .validators import user_register, builder_staff_register
from builders.models import Builder, Manager
from .models import UserStatus


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'sure_name', 'phone')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        # print(user)
        token = super().get_token(user)
        # token['user'] = None
        if user.role.name == 'admin':
            # token['user'] = user.id
            pass
        if user.role.name == 'builder':
            builder = Builder.objects.filter(user=user.id).first()
            print(builder.user_id)

        # if user.role.name == 'manager':
        #     manager = Manager.objects.filter(user=user.id).first()
        #     token['user'] = manager.user

        # token['role'] = user.role.name
        # token['status'] = user.status.name

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        if self.user.role.name == 'admin':
            data['role'] = self.user.role.name
            # data['status'] = self.user.status.name

        elif self.user.role.name == 'builder':
            builder = Builder.objects.select_related('user').filter(user=self.user.id).first()
            builder_serial = BuilderLoginSerializer(builder)
            data['user'] = builder_serial.data
            data['user']['role'] = self.user.role.name
            data['user']['status'] = self.user.status.name

        elif self.user.role.name == 'manager':
            manager = CustomUser.objects.select_related('manager__builder', 'manager__residentcomplex').get(pk=self.user.id)
            manager_serial = ManagerLoginSerializer(manager)
            data['user'] = manager_serial.data
            # data['user']['role'] = self.user.role.name
            # data['user']['status'] = self.user.status.name

        elif self.user.role.name == 'salemanager':
            sale_manager = CustomUser.objects.select_related('status').get(pk=self.user.id)
            sale_serializer = SalerManagerLoginSerializer(sale_manager)
            data['user'] = sale_serializer.data

        return data


class BuilderLoginSerializer(serializers.Serializer):
    image_logo = serializers.ImageField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    sure_name = serializers.CharField(source='user.sure_name')
    # status = serializers.CharField(source='status.name')
    # role = serializers.CharField(source='role.name')
    # status = serializers.BooleanField(source='user.status')


class ManagerLoginSerializer(serializers.Serializer):
    name = serializers.CharField(source="first_name")
    last_name = serializers.CharField()
    surname = serializers.CharField(source="sure_name")
    status = serializers.CharField(source='status.name')
    role = serializers.CharField(source='role.name')
    image_logo = serializers.ImageField(source="manager.builder.image_logo")
    image_banner = serializers.ImageField(source="manager.residentcomplex.image_banner")
    complex_name = serializers.CharField(source="manager.residentcomplex.name")
    complex_id = serializers.IntegerField(source="manager.residentcomplex.id")


class SalerManagerLoginSerializer(serializers.Serializer):
    name = serializers.CharField(source="first_name")
    last_name = serializers.CharField()
    surname = serializers.CharField(source="sure_name")
    status = serializers.CharField(source='status.name')
    role = serializers.CharField(source='role.name')
    # class Meta:
    #     model = Manager
    #     fields = ('name', 'last_name', 'surname', 'image_logo', 'image_banner', 'builder_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    # my_user = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all(),
                                    message="Этот email уже добавлен в базу"
                                    ), ],
    )
    phone = serializers.CharField(max_length=14, required=True,
                                  validators=[UniqueValidator(queryset=CustomUser.objects.all(),
                                                              message="Этот номер уже добавлен в базу"
                                                              )])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'password2', 'email', 'role', 'phone', 'sure_name', 'first_name', 'last_name')

    def validate(self, data):
        error = user_register(data)
        if error:
            raise serializers.ValidationError({'errors': error})
        return data

    def create(self, validated_data):
        data = CustomUser.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            sure_name=validated_data['sure_name']
            # is_staff=True
        )
        data.set_password(validated_data['password'])
        data.save()
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password')
        return representation


class RegisterMangerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all(),
                                    message="Этот email уже добавлен в базу"
                                    ), ],
    )
    phone = serializers.CharField(max_length=14, required=True,
                                  validators=[UniqueValidator(queryset=CustomUser.objects.all(),
                                                              message="Этот номер уже добавлен в базу"
                                                              )])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'password2', 'email', 'role', 'phone', 'sure_name', 'first_name', 'last_name')

    def validate(self, data):
        error = builder_staff_register(data)
        if error:
            raise serializers.ValidationError({'errors': error})
        return data

    def create(self, validated_data):
        data = CustomUser.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            sure_name=validated_data['sure_name'],
            status=UserStatus.objects.filter(name__iexact='active').first()
            # is_staff=True
        )
        data.set_password(validated_data['password'])
        data.save()
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password')
        return representation