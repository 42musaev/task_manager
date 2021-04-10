from django.urls import path

from accounts.api import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view())
]
