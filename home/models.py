from django.db import models

# Create your models here.
class Message(models.Model):
    is_private = models.BooleanField(default=False)
    coutntry_code=models.CharField(max_length=6)
    Number = models.IntegerField()
    Message= models.TextField()

    def __str__(self):
        return self.Message

