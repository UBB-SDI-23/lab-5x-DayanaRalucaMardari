from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', views.getAlbumList, name="album-list"),
    path('id/<str:pk>/', views.getAlbumById, name="album-by-id"),
    path('create/', views.albumCreate, name="album-create"),
    path('update/<str:pk>/', views.albumUpdate, name="album-update"),
    path('delete/<str:pk>/', views.albumDelete, name="album-delete"),
]