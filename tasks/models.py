from django.contrib.auth.models import User
from django.db import models
import uuid


STATUS_CHOICES = (('todo', 'To Do'), ('doing', 'Doing'), ('inreview', 'In Review'), ('done', 'Done'))


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def level_down(self):
        status_list = [x[0] for x in STATUS_CHOICES]
        index = status_list.index("%s" % self.status)
        if index > 0:
            self.status = status_list[index - 1]
            self.save()
        return None

    def level_up(self):
        status_list = [x[0] for x in STATUS_CHOICES]
        index = status_list.index("%s" % self.status)
        if index < len(status_list) - 1:
            self.status = status_list[index + 1]
            self.save()
        return None
