from django.utils.decorators import method_decorator
from tasks import serializers, models, decorators
from rest_framework import viewsets, permissions


@method_decorator(decorators.check_owner, name='update')
@method_decorator(decorators.check_owner, name='destroy')
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.task_set.all()

