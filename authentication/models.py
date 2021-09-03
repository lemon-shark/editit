from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyAccountManager(BaseUserManager):
    # must add required field here
    def create_user(self, email, username, firstname, lastname, birth_year, year, school, postal, level, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            birth_year=birth_year,
            year=year,
            school=school,
            postal=postal,
            level=level
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, birth_year, year, school, postal, level, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            birth_year=birth_year,
            year=year,
            school=school,
            postal=postal,
            level=level
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    firstname = models.CharField(max_length=30, default='fristname')
    lastname = models.CharField(max_length=30, default='lastname')

    birth_year = models.CharField(max_length=30, default='1930')
    year = models.CharField(max_length=30, default='79')
    school = models.CharField(max_length=255, default='default')
    postal = models.CharField(max_length=30, default='V5A 1S6')
    level = models.CharField(max_length=255, default='Other')

    USERNAME_FIELD = 'username'
    # able to add required field here
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname', 'birth_year', 'year', 'school', 'postal', 'level']

    objects = MyAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.username

    def __str__(self):
        return self.school

    def __str__(self):
        return self.level

    class Meta:
        ordering = ['-date_joined']


class School(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Levels'

    def __str__(self):
        return self.name
