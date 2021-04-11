from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.pagination import PageNumberPagination

from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class CreateTaskApp(CreateAPIView):
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    permission_classes = (IsAuthenticated,)


class DetailUpdateDeleteTaskApi(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ListAllTasksApi(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LargeResultsSetPagination


class ListUserTasksApi(ListAllTasksApi):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
