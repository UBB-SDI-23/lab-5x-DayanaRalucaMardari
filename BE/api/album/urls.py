from django.urls import path, include
from . import views

from .views import AlbumList, AlbumDetails, AlbumCreate, \
    AlbumUpdate, AlbumDelete

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', AlbumList.as_view()),
    path('id/<str:pk>/', AlbumDetails.as_view()),
    path('create/', AlbumCreate.as_view()),
    path('update/<str:pk>/', AlbumUpdate.as_view()),
    path('delete/<str:pk>/', AlbumDelete.as_view()),
]