from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):

    def create_user(self, email, contact_number,password=None):
        if not email:
            raise ValueError('User must have an email address')
        

        user = self.model(
            email=self.normalize_email(email),
            contact_number=contact_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contact_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            contact_number=contact_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username=None
    email=models.EmailField(unique=True)
    contact_number=models.IntegerField(default=None,blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['contact_number']
    objects=AccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
