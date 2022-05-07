from django.contrib import admin
from django.urls import path, include
router= routers.DefaultRouter
router.register('User',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]