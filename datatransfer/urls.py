from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('appdata', views.AppdataView)
router.register('localization', views.LocalizationView)

urlpatterns = [
    path('', include(router.urls))
]
