from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('api/', include(router.urls)),
    path('api/posts/info/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('api/posts/new/', views.PostCreate.as_view(), name='post_create'),
    path('api/posts/<int:id>/', views.delete_post, name='delete_post'),
]