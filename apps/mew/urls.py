from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.newgame),
    url(r'^game$', views.game, name="game"),
]
