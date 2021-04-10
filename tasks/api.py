from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class CreateTaskApp(CreateAPIView):
    queryset = Task
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated,)


class DetailUpdateDeleteTaskApi(RetrieveUpdateDestroyAPIView):
    queryset = Task
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated,)
