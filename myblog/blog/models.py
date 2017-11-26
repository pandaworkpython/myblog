from __future__ import unicode_literals

from django.db import models

from django.db.models import Model


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')  # max_length为约束长度，default为默认值
    content = models.TextField(null=True)  # null=True为允许为空
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

