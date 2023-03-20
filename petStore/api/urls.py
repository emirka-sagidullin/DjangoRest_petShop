from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()


router.register(r'order', views.CRUDOrder)
router.register(r'type', views.CRUDType)
router.register(r'status', views.CRUDStatus)
router.register(r'category', views.CRUDCategory)
router.register(r'orderStatus', views.CRUDOrderStatus)
router.register(r'', views.CRUDPet)

urlpatterns = [
    path('', include(router.urls)),
]

