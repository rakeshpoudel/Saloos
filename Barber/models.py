from django.db import models
from myUser.models import CustomUser
from Customer.models import Customer

# Create your models here.
category_choice = (
    ('Accept','Accept'),
    ('Reject','Reject'),
    ('Pending','Pending')
)
class Barber(models.Model):
        name = models.CharField(max_length=100,verbose_name="Barber Name",db_column="Name")
        address = models.CharField(max_length=100,verbose_name="Address")
        contactNo = models.CharField(null=True,blank=True,db_column='contact_no',max_length=15)
        profile = models.ImageField(null=True,blank=True,upload_to='profile/')
        user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

        class Meta:
            db_table = 'barber'

        def __str__(self):
            return self.name

class Service(models.Model):
         barber = models.ForeignKey(Barber,on_delete=models.CASCADE)
         servicetitle = models.CharField(max_length=100,null=True,blank=True)
         description = models.TextField(null=True,blank=True)
         icon = models.ImageField(null=True,blank=True)
         price = models.IntegerField(null=True,blank=True)



         class Meta:
             db_table = 'service'

         def __str__(self):
             return self.barber.name

class Request(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=category_choice)
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        db_table = 'request'

    def __str__(self):
        return self.customer.name