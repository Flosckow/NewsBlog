from PIL import Image
from django.db import models
from django.utils import timezone


class News(models.Model):
    headers = models.CharField(max_length=35)
    publication_date = models.DateTimeField(default=timezone.now())
    body_news = models.TextField(max_length=600)


class Gallery(models.Model):
    image = models.ImageField(upload_to='news', blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)