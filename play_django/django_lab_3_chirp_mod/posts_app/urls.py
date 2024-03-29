# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 3, TWITTER MVP CLONE: https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab03-chirp.md
# PROJECT NAME: chirp_project
# APP NAMES: posts_app, users_app


from django.urls import path
from . import views


# https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
from django.conf.urls import url
# from chirp_project.accounts import views # IS THIS CORRECT? 

# THIS IS THE **POSTS_APP** URLS.PY FILE
app_name = 'posts_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),

    # main chirp stuff:
    path('posts_app/new/', views.PostCreateView.as_view(), name='new_post'),
    path('posts_app/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('posts_app/<int:pk>/edit/', views.PostEditView.as_view(), name='edit_post'),
    path('posts_app/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),

    # change password:
    url(r'^password/$', views.change_password, name='change_password'),

    # comments:    
    path('posts_app/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    
    # path('', views.xxx, name=''),
]
