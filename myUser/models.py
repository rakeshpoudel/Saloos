from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,contactNo,password=None):
        if not email:
            raise ValueError("email is required")
        user = self.model(
            email= self.normalize_email(email),
            contactNo = contactNo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,contactNo,password=None):
        user = self.create_user(email,contactNo,password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email Address",
        unique=True,
    )
    contactNo = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contactNo']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

