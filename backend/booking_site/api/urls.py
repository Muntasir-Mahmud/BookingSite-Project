from django.urls import path
from .views import HotelList, HotelDetail



urlpatterns = [
    path('<int:pk>/', HotelDetail.as_view()),
    path('', HotelList.as_view()),
]
