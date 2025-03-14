from django.contrib.auth import models as auth_models
from django.db import models


class UserManager(auth_models.BaseUserManager):
    def create_user(self, username: str, melli_code: str, phone_number: str, is_staff=False, is_superuser=False):
        if not phone_number:
            raise ValueError('user must have Phone Number')

        if not username:
            raise ValueError('user must have username')

        if not melli_code:
            raise ValueError('user must have Melli Code')

        user = self.model(phone_number=phone_number, username=username, melli_code=melli_code)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, username: str, melli_code: str, phone_number: str, password: str = None):
        user = self.create_user(
            username=username,
            melli_code=melli_code,
            phone_number=phone_number,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()
        return user

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

    #objects = UserManager()

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
