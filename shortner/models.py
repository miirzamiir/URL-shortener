import uuid
from django.db import models

class Link(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)