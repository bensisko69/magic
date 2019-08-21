from django.urls import path

from . import views

urlpatterns = [
    path('add/card', views.index, name='addCard'),
    path('search', views.search, name='search'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('import', views.importCard, name='importCard'),
    path('resultCard', views.resultCard, name='resultCard'),
    path('addCard', views.addCard, name='addCard'),
    path('createDecks', views.createDecks, name='createDecks'),
    path('decks', views.decks, name='decks'),
    path('', views.index, name='index'),
]