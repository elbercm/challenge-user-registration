
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models


class UsuarioManager(BaseUserManager):

  def create_user(self, email, password=None):
    user = self.model(
        email=self.normalize_email(email)
    )
    user.is_active = True
    user.is_staff = False
    user.is_superuser = False

    if password:
      user.set_password(password)

    user.save()

    return user

  def create_superuser(self, email, password):
    user = self.create_user(
        email=self.normalize_email(email),
        password=password,
    )

    user.is_active = True
    user.is_staff = True
    user.is_superuser = True

    user.set_password(password)

    user.save()

    return user


class User(AbstractBaseUser, PermissionsMixin):

  name = models.CharField(max_length=80, verbose_name='name')
  email = models.EmailField(verbose_name="E-mail do usuário", max_length=194, unique=True)
  cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
  pis = models.CharField(max_length=14, unique=True, verbose_name='PIS')
  endereco = models.CharField(max_length=60, verbose_name='Endereço')
  numero = models.CharField(max_length=7, verbose_name='Nº')
  complemento = models.CharField(max_length=30, verbose_name='Complemento', blank=True, null=True)
  bairro = models.CharField(max_length=50, verbose_name='Bairro')
  cep = models.CharField(max_length=9, verbose_name='CEP')
  pais = models.CharField(max_length=40, verbose_name='País')
  cidade = models.CharField(max_length=40, verbose_name='Cidade')
  estado = models.CharField(
      verbose_name='Estado',
      max_length=19,
      default='São Paulo',
      choices=(
          ('Acre', 'Acre'),
          ('Alagoas', 'Alagoas'),
          ('Amapá', 'Amapá'),
          ('Amazonas', 'Amazonas'),
          ('Bahia', 'Bahia'),
          ('Ceará', 'Ceará'),
          ('Distrito Federal', 'Distrito Federal'),
          ('Espírito Santo', 'Espírito Santo'),
          ('Goiás', 'Goiás'),
          ('Maranhão', 'Maranhão'),
          ('Mato Grosso', 'Mato Grosso'),
          ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
          ('Minas Gerais', 'Minas Gerais'),
          ('Pará', 'Pará'),
          ('Paraíba', 'Paraíba'),
          ('Paraná', 'Paraná'),
          ('Pernambuco', 'Pernambuco'),
          ('Piauí', 'Piauí'),
          ('Rio de Janeiro', 'Rio de Janeiro'),
          ('Rio Grande do Norte', 'Rio Grande do Norte'),
          ('Rio Grande do Sul', 'Rio Grande do Sul'),
          ('Rondônia', 'Rondônia'),
          ('Roraima', 'Roraima'),
          ('Santa Catarina', 'Santa Catarina'),
          ('São Paulo', 'São Paulo'),
          ('Sergipe', 'Sergipe'),
          ('Tocantins', 'Tocantins'),
      )
  )

  def __str__(self):
    return f'{self.name}'

  def clean(self):
    error_messages = {}

    if error_messages:
      raise ValidationError(error_messages)

  is_active = models.BooleanField(
      verbose_name="Usuário está ativo",
      default=True,
  )

  is_staff = models.BooleanField(
      verbose_name="Usuário é da equipe de desenvolvimento",
      default=False,
  )

  is_superuser = models.BooleanField(
      verbose_name="Usuário é um superusuario",
      default=False,
  )

  USERNAME_FIELD = "email"

  objects = UsuarioManager()

  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"
    db_table = "user"
