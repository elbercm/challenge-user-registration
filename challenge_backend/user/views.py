from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.middleware import csrf
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView


from .serializers import (
    CadastroUsuarioSerializer, UsuarioLogadoSerializer, UpdateUserSerializer)


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)

  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class RegisterUserView(CreateAPIView, APIView):
  queryset = get_user_model().objects.all()
  permission_classes = (AllowAny,)
  serializer_class = CadastroUsuarioSerializer

  # Cadastrar Usuario no banco
  def post(self, request):
    print('request.data', request.data)
    try:
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      user.is_active = True
      user.set_password(user.password)
      user.save()
      return Response(
          data=get_tokens_for_user(user),
          status=status.HTTP_201_CREATED
      )
    except Exception as e:
      return Response(
          data={'error': str(e).replace("User", "Usuário")},
          status=status.HTTP_400_BAD_REQUEST
      )


class UpdateUserView(APIView):
  permission_classes = (IsAuthenticated, )

  def put(self, request):
    serializer = UpdateUserSerializer(request.user, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


class DeleteUserView(APIView):
  permission_classes = (IsAuthenticated, )

  def delete(self, request):
    request.user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
  def post(self, request, format=None):
    data = request.data
    response = Response()
    email = data.get('email', None)
    password = data.get('password', None)
    user = authenticate(email=email, password=password)
    if user is not None:
      if user.is_active:
        data = get_tokens_for_user(user)
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=data["access"],
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        csrf.get_token(request)
        response.data = {"Success": "Login successfully", "data": data}

        return response
      else:
        return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
    else:
      return Response({"Invalid": "Invalid email or password!!"}, status=status.HTTP_404_NOT_FOUND)


class UserLoggedView(ModelViewSet):
  queryset = get_user_model().objects.all()
  permission_classes = (IsAuthenticated,)
  serializer_class = UsuarioLogadoSerializer

  def retrieve(self, request, *args, **kwargs):
    usuario_logado = self.queryset.get(email=request.user.email)
    serializer = self.get_serializer(usuario_logado)
    return Response({'usuario': serializer.data})
