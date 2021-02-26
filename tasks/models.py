from django.contrib.auth.models import User
from django.db import models
import uuid


STATUS_CHOICES = (('todo', 'To Do'), ('doing', 'Doing'), ('inreview', 'In Review'), ('finished', 'Finished'))


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.name
