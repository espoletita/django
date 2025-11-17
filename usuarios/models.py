from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, telefone, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        if not nome:
            raise ValueError("O nome é obrigatório")
        if not telefone:
            raise ValueError("O telefone é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, telefone=telefone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, telefone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nome, telefone, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    nome = models.CharField('Nome completo', max_length=150)
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'telefone']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email
