from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FilesTemp(models.Model):
    filetemp = models.FileField('arquivo',upload_to='uploads/')
    pub_date = models.DateField(auto_now=True)
    pub_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.filetemp

    class Meta:
        ordering = ['pub_date','pub_time']
        verbose_name = 'filetemp'
        verbose_name_plural = 'filestemp'