from django.contrib.auth import models as auth_models
from django.db import models
from .managers import UserManager



class UserModel(auth_models.AbstractUser):
    full_name = models.CharField(max_length=35, verbose_name="نام کامل")
    study_field = models.CharField(max_length=50, verbose_name="رشته تحصیلی")
    username = models.CharField(max_length=20, unique=True, verbose_name="نام کاربری")
    melli_code = models.CharField(max_length=20, unique=True, verbose_name="کد ملی")
    phone_number = models.CharField(max_length=12, unique=True, verbose_name="شماره تلفن")
    password = models.CharField(max_length=255, null=True, verbose_name="رمز عبور")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'melli_code']

    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.username:
            return self.username
        return self.pk

class OtpModel(models.Model):
    phone_number = models.CharField(max_length=12)
    otpCode = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return f"{self.phone_number} | {self.otpCode}"
