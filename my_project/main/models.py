from django.db import models
from django.conf import settings


# Create your models here.
class Gig(models.Model):
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_time = models.IntegerField(help_text="Delivery time in days")
    image = models.ImageField(upload_to='gig_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
