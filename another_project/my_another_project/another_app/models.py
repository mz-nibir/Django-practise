from django.db import models

# Create your models here.

class Musician (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument =models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Albam (models.Model):
    artist = models.ForeignKey(Musician, on_delete= models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()



    rating= (
    (1,'worst'),
    (2,'bad'),
    (3,'not bad'),
    (4,'good'),
    (5,'Excellent!'),
    )
    num_stars= models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + ", rating: "+ str(self.num_stars)
