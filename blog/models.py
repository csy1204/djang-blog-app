from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    # null 과 blank의 차이점: blank는 validation을 요구하지 않는다!
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url