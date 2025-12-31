from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    review = models.CharField(max_length=250, null=True, blank=True)
    img_url = models.URLField(max_length=250)

    def __str__(self):
        return self.title