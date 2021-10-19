from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email, password):
        user = self.create_user(
            email = email,
            password=password,
        )
        user.is_admin = False,
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password):
        user = self.create_user(
            username,
            email,
            password
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser): 
    ...
    objects = UserManager()

class Usuario(AbstractUser):
    foto = models.CharField(
        verbose_name='foto de perfil',
        max_length=500,
        blank = False, 
        null = False,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Correo electronico',
        unique=True,
    )
    gris_disponible = models.BooleanField(
        verbose_name='gris_disponible',
        blank=False,
        default=True,
    )
    azul = models.IntegerField(default=0)
    naranja = models.IntegerField(default=0)
    dorado = models.IntegerField(default=0)
    equipo = models.ForeignKey('Equipo',null=True,on_delete=models.SET_NULL)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','foto']

    def __str__(self):
        return self.username 

class Equipo(models.Model):
    numero = models.IntegerField()
    name = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.name
