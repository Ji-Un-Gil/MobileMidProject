from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('api/posts/', views.PostViewSet, name='post_view_set'),
    path('api/posts/info/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('api/posts/new/', views.PostCreate.as_view(), name='post_create'),
    path('api/posts/<int:id>/', views.delete_post, name='delete_post'),
]