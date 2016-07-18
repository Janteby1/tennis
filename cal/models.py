from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone #make sure to set the timezone 
from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Scores(models.Model):
    player = models.CharField (max_length=120)
    court = models.IntegerField(default = 0)
    won = models.IntegerField(default = 0)
    loss = models.IntegerField(default = 0)
    created_at = models.DateTimeField(default = timezone.now, editable=False)
    show = models.BooleanField(default=True)

    def to_json(self):
        return {
            "id": self.id,
            "player": self.player,
            "court": self.court,
            "won": self.won,
            "loss": self.loss,
            "created_at": self.created_at,
            "show": self.show,
        }







