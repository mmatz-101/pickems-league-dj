from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"pk": self.pk})
