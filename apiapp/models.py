from django.db import models

# Create your models here.

class Posts(models.Model):
    regions = models.CharField(max_length=30)
    districts= models.TextField(max_length=2000)
    
    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
     
    def __str__(self):
        return self.regions
