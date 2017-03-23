from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
    content     = models.TextField()

    def __str__(self):
         return str(self.content)
