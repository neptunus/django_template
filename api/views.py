from api.models import Post
from api.serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions

class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new one
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
