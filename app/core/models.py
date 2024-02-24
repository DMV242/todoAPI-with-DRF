from django.db import models
from django.contrib.auth import get_user_model

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(),models.CASCADE,null=True)

    def __str__(self):
        return self.title
