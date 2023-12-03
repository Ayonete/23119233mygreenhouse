from django.db import models

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField (max_length= 300)
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    temperature = models.DecimalField(max_digits=4, decimal_places= 2)
    moisture = models.DecimalField(max_digits=4, decimal_places= 2)
    planted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    # this is the string representation
    # what to display after querying a crop/crops
    def __str__(self):
        return f'{self.name}'
    
    # this will order the crops by date created
    class Meta:
        ordering = ['-planted_on']