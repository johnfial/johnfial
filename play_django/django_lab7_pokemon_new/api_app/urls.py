from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, TypeViewSet, UserViewSet, CurrentUserView

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon' ) # register the pokemon
router.register('users', UserViewSet, basename='users')
router.register('type', TypeViewSet, basename='type')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view()),
]
