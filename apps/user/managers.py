from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        password=None,
        is_active=True,
        is_staff=False,
        is_admin=False,
    ):
        if not email:
            raise ValueError("Must have Email")
        if not username:
            raise ValueError("Must have Username")
        if not password:
            raise ValueError("Must have Password")

        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, password=None):
        if not email:
            raise ValueError("Must have Email")
        if not password:
            raise ValueError("Must have Password")

        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_active=True,
        )

        return user

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError("Must have Email")
        if not username:
            raise ValueError("Must have Username")
        if not password:
            raise ValueError("Must have Password")
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        return user