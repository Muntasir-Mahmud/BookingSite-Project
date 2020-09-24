from django.urls import path, include
from .views import HotelList, HotelDetail



urlpatterns = [
    path('<int:pk>/', HotelDetail.as_view()),
    path('', HotelList.as_view()),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
