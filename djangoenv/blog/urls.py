from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('api_root/', include(router.urls)),
    path('api/', include(router.urls)),
]