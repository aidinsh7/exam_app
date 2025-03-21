from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
    def create_user(self, username: str, melli_code: int, phone_number: int, is_staff=False, is_superuser=False):
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

    def create_superuser(self, username: str, melli_code: int, phone_number: int, password: str ):
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


