from django.db import models
from django.contrib.auth.models import User
import uuid

class TodoTask(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100,null=False)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
