from django.urls import include, path
from rest_framework import routers

from task import views


router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)


urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('', include(router.urls)),
]
