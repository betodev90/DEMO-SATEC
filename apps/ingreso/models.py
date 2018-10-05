from django.db import models

# Create your models here.
# from __future__ import unicode_literals
#from django_extensions.db.models import TimeStampedModel
#from audit_log.models import AuthStampedModel
# from django.db import models
# from django.contrib.auth.models import User
# from livefield import LiveModel
# from django.db.models.fields.related import OneToOneField
# from roman import toRoman
# from django.db.models.deletion import CASCADE
# from django.db.models.fields import BooleanField


class Country(models.Model):

    class Meta:
        verbose_name = 'país'
        verbose_name_plural = 'países'
        db_table = 'sigia_country'

    name = models.CharField(max_length=50, unique=True, verbose_name="nombre")
    gentilicio = models.CharField(max_length=50, verbose_name="nacionalidad")

    def __str__(self):
        return "%s" % self.name