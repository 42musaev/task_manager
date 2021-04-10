from django.urls import path

from tasks.api import TaskApi

urlpatterns = [
    path('create/', TaskApi.as_view())
]
