from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User  # necessary? # TODO

from pokemon.models import Pokemon, Type

# NESTED:
class NestedUserSerializer(serializers.ModelSerializer):
    # goal here was to print 'self.id' ...
    # print(f"I'm printing an f-string inside the api_app/serializers.py file with the self ~CLIPPED~.")# :{self} | and the self.id, self.username: {self.id}, {self.username}.")
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',) # NOTE removed: 'username'

# NESTED:
class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'type', 'pokemon', )

# NESTED:
class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type', 'caught_by', ) # should not have 'caught_by' field here, right?

# # # # # # # # # # # # # # # 

class UserSerializer(serializers.ModelSerializer):
    # post_detail = NestedPostSerializer(read_only=True, many=True, source='post_set')
    
    # I don't understand this _detail variable. ...
    # I don't understand this pokemon_set variable, or what the (source='') argument does from the NestedXYZSerializer...
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True, source='pokemon_set')
    class Meta:
        model = get_user_model()
        fields = ('id', 'pokemon_detail', 'pokemon_set', 'username') # Why 'date_joined' and where does it come from? Automatic with custom user model?
        # NOTE removed 

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True, source='pokemon_set')
    class Meta:
        model = Type
        fields = ('id', 'type', 'pokemon', 'pokemon_detail')

class PokemonSerializer(serializers.ModelSerializer):
    type = NestedTypeSerializer(read_only=True)
    caught_by = NestedUserSerializer(read_only=True, source='username')
         #NOTE fix? , source='caught_by')
         # NO, see error: id
            #  AssertionError at /api/v1/pokemon/ 
            # It is redundant to specify `source='caught_by'` on field 'NestedUserSerializer' in serializer 'PokemonSerializer', because it is the same as the field name. Remove the `source` keyword argument.
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'type', ) # nick also has 'username_detail'


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