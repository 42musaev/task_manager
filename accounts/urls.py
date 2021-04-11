from django.urls import path

from accounts.api import CreateUserView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='account_register'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
