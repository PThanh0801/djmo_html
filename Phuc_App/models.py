from django.db import models

# Create your models here.
class Baibao(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField(blank=True)
    image = models.URLField(max_length = 200)
    #image = models.ImageField(null=True,blank=True,upload_to="images/")

    class Meta:
        db_table = "StoreArt"