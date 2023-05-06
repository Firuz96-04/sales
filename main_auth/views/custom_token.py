from rest_framework_simplejwt.views import TokenObtainPairView

from main_auth.serializers import MyTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer