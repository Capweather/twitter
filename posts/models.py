from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'



    name = models.CharField(
        'Name', blank= True, null =True, max_length = 14, db_index = True, default = 'Anonymous'

)

    body = models.CharField(
    'Body', blank =  True, null = True, max_length = 140, db_index= True

)

    created_at = models.DateTimeField(
        'created_Datetime', blank=True, auto_now_add= True

)

    image = CloudinaryField(
        'image', blank=True,null=True

)
    likes = models.PositiveIntegerField(
        'like', blank = True , null = True , default = 0 
)
    
