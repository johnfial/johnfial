from django.urls import path # /APP URLS APP

from . import views

app_name = 'example' # this can be different from the folder name, and some references point to this
urlpatterns = [
    path('', views.index, name='index'), # 3 parameters for each 'route': index page/default, the , and the name (optional)
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]