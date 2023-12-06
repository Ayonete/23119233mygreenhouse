# from django.db import models

# # Create your models here.
# class Crop(models.Model):
#     name = models.CharField(max_length= 100)
#     description = models.TextField (max_length= 300)
#     image = models.ImageField(null=False, blank=False, upload_to='images/')
#     temperature = models.DecimalField(max_digits=4, decimal_places= 2)
#     moisture = models.DecimalField(max_digits=4, decimal_places= 2)
#     planted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
#     # this is the string representation
#     # what to display after querying a crop/crops
   
#     def __str__(self):
#         return f'{self.name}'
    
#     # this will order the crops by date created
#     class Meta:
#         ordering = ['-planted_on']
from django.db import models
import boto3
from boto3 import resource

class Crop(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    planted_on = models.TextField(max_length=200, default="20/20/20")
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    moisture = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        super(Crop, self).save(*args, **kwargs)
        dynamodb = boto3.resource('dynamodb')
        resources = resource('dynamodb',
                               aws_access_key_id     = 'ASIA5NI3FLPMG7WXKD5I',
                               aws_secret_access_key = 'TjsEkHEAVT0RQOxBvp4WqKVpiYH5bOnPRS62pPnB',
                               region_name           = 'us-east-1'
       )      
       
        table = dynamodb.Table('23119233-greenhouse-records')
        table.put_item(
            Item={
                'name': self.name,
                'planted_on': self.planted_on,
                'description': self.description,
                'temperature': str(self.temperature),  # Convert DecimalField to string
                'moisture': str(self.moisture),   
                'image': self.image
                # Convert DecimalField to string
            }
        )

    # def save(self, *args, **kwargs):
    #     # Save the instance as usual
    #     super(Crop, self).save(*args, **kwargs)
        
    #     # Insert record into DynamoDB
    #     dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id= 'ASIA5NI3FLPMG7WXKD5I',  aws_secret_access_key = 'TjsEkHEAVT0RQOxBvp4WqKVpiYH5bOnPRS62pPnB')
    #     table = dynamodb.Table('23119233-greenhouse-records')
    #     print(table)
    #     try:
    #         table.put_item(
    #             Item={
    #                 'name': self.name,
    #                 'planted_on': self.planted_on,
    #                 'description': self.description,
    #                 'temperature': str(self.temperature),  # Convert DecimalField to string
    #                 'moisture': str(self.moisture),   
    #                 'image': self.image
    #                 # Convert DecimalField to string
    #             }
    #         )
    #     except Exception as e:
    #     # Handle the exception (log it, alert, etc.)
    #         print(f"Error inserting record into DynamoDB: {e}")
    
class Diagnostics(models.Model):
    # Dropdown choices for 'appearance'
    crop_name = models.CharField(max_length= 100)
    APPEARANCE_CHOICES = [
        ('SPOT', 'Spotted'),
        ('YELLOW', 'Yellowing'),
        ('WILT', 'Wilting'),
        ('HEALTHY', 'Healthy'),
    ]

    # Dropdown choices for 'leaf_age'
    LEAF_AGE_CHOICES = [
        ('YOUNG', 'Young'),
        ('MATURE', 'Mature'),
        ('OLD', 'Old'),
    ]

    appearance = models.CharField(max_length=7, choices=APPEARANCE_CHOICES, default='HEALTHY')

    leaf_age = models.CharField(max_length=6, choices=LEAF_AGE_CHOICES, default='MATURE')