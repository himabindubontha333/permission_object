from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

class EditorPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = 'Editor Permission'
        verbose_name_plural = 'Editor Permissions'

class AdminPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = 'Admin Permission'
        verbose_name_plural = 'Admin Permissions'

class ViewerPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = 'Viewer Permission'
        verbose_name_plural = 'Viewer Permissions'

class CreatorPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = 'Creator Permission'
        verbose_name_plural = 'Creator Permissions'
  


