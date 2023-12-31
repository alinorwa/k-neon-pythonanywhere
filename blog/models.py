from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
