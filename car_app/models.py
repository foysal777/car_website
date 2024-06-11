from django.db import models

# Create your models here.

class BrandModel(models.Model):
    brand_name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100 , unique=True,  blank=True , null= True)
    
    def __str__(self):
        return self.brand_name
    
    


class CarModel(models.Model):
    car_name = models.CharField(max_length=20)
    brand = models.ForeignKey(BrandModel , related_name='cars' , on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10 , decimal_places=3)
    image = models.ImageField(upload_to='car_app/media/', blank=True , null= True)
    des = models.CharField(max_length=100 , unique=True,  blank=True , null= True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
       return self.car_name
       
       
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel , on_delete=models.CASCADE , related_name='cmt' , null=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    comment_here = models.TextField(max_length=100)
    show_date = models.DateTimeField(auto_now_add=True)      
    
    
    def __str__(self):
        return self.name
    