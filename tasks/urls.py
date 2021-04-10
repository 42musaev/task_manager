from django.urls import path

from tasks.api import CreateTaskApp, DetailUpdateDeleteTaskApi

urlpatterns = [
    path('create/', CreateTaskApp.as_view()),
    path('<int:pk>/', DetailUpdateDeleteTaskApi.as_view())
]
