from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import *
router = DefaultRouter(trailing_slash=False)
router.register(r'city', CityApiView, basename='city')
router.register(r'elevator', ElevatorApiView, basename='elevator')
router.register(r'parking', ParkingApiView, basename='parking')
router.register(r'kitchen', KitchenApiView, basename='kitchen')
router.register(r'decoration', DecorationApiView, basename='decoration')
router.register(r'facade', FacadeApiView, basename='facade')
router.register(r'heating', HeatingApiView, basename='heating')
router.register(r'building-type', BuildingTypeApiView, basename='building-type')
router.register(r'floor-type', FloorTypeApiView, basename='floor-type')
router.register(r'apartment-decoration', ApartmentDecorationApiView, basename='apartment-decoration')
router.register(r'sale-manager-action', SaleManagerActionApiView, basename='sale-manager-action')
# print(router.urls)
urlpatterns = [
    path('', include(router.urls)),
    # path('city/<int:pk>/', CityApiView.as_view({'delete': 'destroy'})),
    path('region/', RegionApiView.as_view()),
    path('regionstree/', RegionListApiView.as_view())
]