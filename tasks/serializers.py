from rest_framework import serializers
from tasks import models


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Task
        fields = ('id', 'name', 'content', 'status')
