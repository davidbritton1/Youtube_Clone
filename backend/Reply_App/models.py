from django.db import models
from authentication.models import User
# from django.contrib.auth.models import User


class Reply(models.Model):
    reply_user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)