from api.models import Post
from api.serializers import PostSerializer
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new one
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
