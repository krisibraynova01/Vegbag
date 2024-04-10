from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.URLField()
    author = models.CharField(max_length=200, null=False, blank=False)
    short_description = models.TextField()


    def __str__(self):
        return self.title
