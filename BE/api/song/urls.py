from django.urls import path, include
from . import views
from .views import SongList, SongDetails, SongCreate, \
    SongUpdate, SongDelete

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', SongList.as_view()),
    path('id/<str:pk>/', SongDetails.as_view()),
    path('create/', SongCreate.as_view()),
    path('update/<str:pk>/', SongUpdate.as_view()),
    path('delete/<str:pk>/', SongDelete.as_view()),
]