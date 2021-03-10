from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from auth import api_views

app_name = 'auth'

urlpatterns = [
    path('login/', api_views.LoginView.as_view(), name='login'),
    path('signup/', api_views.CreateUserView.as_view(), name='signup'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh')
]
