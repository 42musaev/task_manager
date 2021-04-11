from django.urls import path

from tasks.api import (
    CreateTaskApp,
    DetailUpdateDeleteTaskApi,
    ListAllTasksApi,
    ListUserTasksApi
)

urlpatterns = [
    path('', ListAllTasksApi.as_view()),
    path('<int:pk>/', DetailUpdateDeleteTaskApi.as_view()),
    path('my-tasks/', ListUserTasksApi.as_view()),
    path('create/', CreateTaskApp.as_view()),
]
