from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from main_auth.views import *


router = SimpleRouter()


urlpatterns = [
    path('manager-register/', RegisterManagerApiView.as_view({'post': 'create'})),
    path('salemanager-register/', RegisterSaleManager.as_view())
    # path('', UserApiView.as_view()),
    # path('manager-register/', RegisterBuilderStaff.as_view()),
    # path('test/', TesAPiView.as_view())
    # path('build/<int:pk>/', BuilderApiViewUpd.as_view())
]