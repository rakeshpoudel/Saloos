from django.db import models
from myUser.models import CustomUser
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name",db_column="Customer Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    contactNo = models.CharField(null=True, blank=True, db_column='contact_no', max_length=15)
    profile = models.ImageField(null=True, blank=True, upload_to='profile/')
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name




