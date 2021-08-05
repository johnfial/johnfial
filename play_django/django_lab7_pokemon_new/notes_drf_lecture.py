# notes from library example monday 2 aug 2021:
# https://github.com/PdxCodeGuild/class_salmon/blob/main/4%20Django/labs/lab04-library.md
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# make books app
# class Book
    # with title, subtitle, author, isbn (char field and not int)

# create superuser
# create admin
    # admin.py from .models import Class
    # admin.site.register(Class)
# runserver
# add books as admin

# views.py:
    # imports... Class, models, 

# urls.py   
    # imports
    # urlpatterns ()



# create a book_list template .html
    # for book in object_list
    # ul, 
    # endfor 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# DJANGO REST FRAMEWORK NOTES
# best to specify version!
    # https://www.django-rest-framework.org/community/release-notes/ 
    # 3.12.x
    
# pipenv install djangorestframework==3.12

# INSTALL INTO DJANGO:
    # settings INSTALLED_APPS
        # 'rest_framework',

# NOTE: HIGHLY RECCOMENDED to have all the API code in its own django 'app'
    # python manage.py startapp api_app
    # add to settings.py INSTALLED_APPS
    # project urls.py
        # include api urls.py, set paths...
    # api_app views.py
        # import Book, import BookSerializer, import generics
        # class BookAPIView(generics)
    # api_app serializers.py 
        # see my old https://github.com/PdxCodeGuild/class_orca/tree/main/code/john/django_labs/django_lab_6_dec21_REST_framework_and_VUE
        # import serializers, Book Class, 
        # class BookSerializer(serializers.ModelSerializer)
            # class Meta:
                # model = Book
                # fields = ['title', 'otherfield', . . . ]

# CLI:
    # curl localhost:8000/api_app
    # try ... -X options
    # or ... -X head
    # browsable API from django look good, django pretti-fies it!
    # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# NEW PROJECT -- REST API FOR VUE, RIGHT? NEW PROJECT FOR DRF-BLOG
# copy posts project?
# urls.py . . ., views.py:
# Class PostList(generics.ListCreateAPIView)
    # list/create DO NOT NEED pks
    # create/update DO REQUIRE pks

# rememmber PUT/PATCH
    #put REQUIRES EVERY FIELD IN THE MODEL
    #patch allows partial changes...

# # lunch break
# # lunch break
# # lunch break
# # lunch break

# REST_FRAMEWORK stuff in proj/settings.py
# ----------------------


# django CORS headers
# search, find, install pip
# put in settings.py INSTALLED_APSS, MIDDLEWARE [], 
