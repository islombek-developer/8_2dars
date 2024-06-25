from django.db import models


    
class News(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    content = models.TextField()


    def __str__(self):
        return self.name
