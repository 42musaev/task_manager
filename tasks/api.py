from rest_framework.generics import CreateAPIView

from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskApi(CreateAPIView):
    queryset = Task
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
