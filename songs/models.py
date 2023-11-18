from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year = models.IntegerField()
    cover = models.URLField(max_length=200, null=True)
    lyrics = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.artist} - {self.title} ({self.year})'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
class Category(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    songs = models.ManyToManyField(Post)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.description} by {self.author}'