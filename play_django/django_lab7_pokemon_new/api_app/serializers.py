from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User  # necessary? # TODO

from pokemon.models import Pokemon

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
    # goal here was to print 'self.id' ...
    # print(f"I'm printing an f-string inside the api_app/serializers.py file with the self ~CLIPPED~.")# :{self} | and the self.id, self.username: {self.id}, {self.username}.")

class UserSerializer(serializers.ModelSerializer):
    # post_detail = NestedPostSerializer(read_only=True, many=True, source='post_set')
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',) # 'date_joined', 'post_set', 'post_detail'

# # # # # # # # # # # # # # # 

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', ) # should not have 'caught_by' field here, right?

class PokemonSerializer(serializers.ModelSerializer):
    caught_by = NestedUserSerializer(read_only=True) #NOTE fix? , source='caught_by')
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by',)




# from https://www.django-rest-framework.org/tutorial/quickstart/ :
# nested user serializer, pokemon serializer...
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# merritt drf-blog: 
    # from rest_framework import serializers
    # from django.contrib.auth import get_user_model

    # from posts.models import Post

    # class NestedPostSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Post
    #         fields = ('id', 'title', 'created', 'updated', 'body')

    # class NestedUserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = ('id', 'username')

    # class PostSerializer(serializers.ModelSerializer):
    #     author_detail = NestedUserSerializer(read_only=True, source='author')
    #     class Meta:
    #         model = Post
    #         fields = ('id', 'title', 'author', 'author_detail', 'created', 'updated', 'body')

    # class UserSerializer(serializers.ModelSerializer):
    #     post_detail = NestedPostSerializer(read_only=True, many=True, source='post_set')
    #     class Meta:
    #         model = get_user_model()
    #         fields = ('id', 'username', 'date_joined', 'post_set', 'post_detail')