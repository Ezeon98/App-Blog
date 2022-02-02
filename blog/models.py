from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)

    def __str__(self): ##Con esto me trae el titulo del post en el panel de admin
        return self.title
    