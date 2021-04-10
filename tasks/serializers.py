from rest_framework.serializers import ModelSerializer

from tasks.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'user',
            'name',
            'description',
            'date_end',
            'file'
        ]
