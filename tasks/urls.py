from django.urls import path

from tasks.api import (
    CreateTaskApp,
    DetailUpdateDeleteTaskApi,
    ListAllTasksApi,
    ListUserTasksApi
)

urlpatterns = [
    path('', ListAllTasksApi.as_view()),
    path('<int:pk>/', DetailUpdateDeleteTaskApi.as_view(), name='task_detail'),
    path('my-tasks/', ListUserTasksApi.as_view()),
    path('create/', CreateTaskApp.as_view(), name='task_create'),
]
