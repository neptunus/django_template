from api.models import Post
from api.serializers import PostSerializer
from rest_framework import mixins
from rest_framework import generics


class PostList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    """
    List all posts, or create a new one
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    """
    Retrieve, update or delete a post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


