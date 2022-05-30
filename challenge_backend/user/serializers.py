from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import User


class CadastroUsuarioSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = "__all__"
    extra_kwargs = {
        'password': {'write_only': True},
    }


class UpdateUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
        'name', 'email', 'cpf', 'pis', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'pais', 'cidade', 'estado',
    )


class UsuarioLogadoSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    return get_user_model().objects.create_user(**validated_data)

  class Meta:
    model = get_user_model()
    fields = "__all__"
    extra_kwargs = {
        'password': {'write_only': True},
    }
