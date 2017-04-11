from django.db import models
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网址',max_length=256)
    