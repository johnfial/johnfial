from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon
from .serializers import PokemonSerializer, UserSerializer 
from .permissions import IsAuthorOrReadOnly

# UserViewSet, PokeMonViewSet, CurrentUserView? . . . 
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_class = [IsAuthorOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# merritt drf-blog: 
    # from rest_framework import generics, viewsets
    # from django.contrib.auth import get_user_model

    # from posts.models import Post
    # from .serializers import PostSerializer, UserSerializer
    # from .permissions import IsAuthorOrReadOnly

    # class PostViewSet(viewsets.ModelViewSet):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer
    #     permission_classes = [IsAuthorOrReadOnly]

    # class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #     queryset = get_user_model().objects.all()
    #     serializer_class = UserSerializer

    # class CurrentUserView(generics.RetrieveAPIView):
    #     serializer_class = UserSerializer
    #     def get_object(self):
    #         return self.request.user

    # # class PostList(generics.ListCreateAPIView):
    # #     queryset = Post.objects.all()
    # #     serializer_class = PostSerializer
    # #     permission_classes = [IsAuthorOrReadOnly]

    # # class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # #     queryset = Post.objects.all()
    # #     serializer_class = PostSerializer
    # #     permission_classes = [IsAuthorOrReadOnly]