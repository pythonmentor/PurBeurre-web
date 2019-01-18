from django.urls import path

from . import views

urlpatterns = [
    path('api/save_favorite/', views.save_favorite, name='save-favorite'),
    path('favorite-list/', views.FavoriteList.as_view(), name='favorite-list'),
]
