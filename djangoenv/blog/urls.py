from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('api/posts/<int:id>/', views.delete_post, name='delete_post'),
    path('api/posts/info/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('api/posts/new/', views.PostCreate.as_view(), name='post_create'),
    path('api/', include(router.urls)),
]