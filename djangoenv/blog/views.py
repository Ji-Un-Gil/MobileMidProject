from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404

from .serializers import PostSerializer

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/post_list.html", {'posts': posts})


@csrf_exempt
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return JsonResponse({"message": "게시물이 삭제되었습니다."})
    except Post.DoesNotExist:
        return JsonResponse({"error": "게시물을 찾을 수 없습니다."}, status=404)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_url_kwarg: self.kwargs[self.lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class PostCreate(CreateAPIView):
    serializer_class = PostSerializer

