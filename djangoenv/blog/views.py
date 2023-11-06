from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404
from rest_framework.response import Response

from .serializers import PostSerializer

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/post_list.html", {'posts': posts})


@api_view(['DELETE'])
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response({}, status=204)
    except Post.DoesNotExist:
        return Response({}, status=404)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
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


@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

