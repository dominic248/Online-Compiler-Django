from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, password=None, *args, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        print("User Created (user): ", args, kwargs)
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, password, *args, **kwargs):
        """
        Creates and saves a staff user with the given email and password.
        """
        print("User Created (staffuser): ", args, kwargs)
        user = self.model(**kwargs)
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, password, *args, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        print("User Created (superuser): ", args, kwargs)
        user = self.model(**kwargs)
        user.set_password(password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
