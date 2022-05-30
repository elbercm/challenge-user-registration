from django.urls import path
from .views import LoginView, RegisterUserView, UserLoggedView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('user/', UserLoggedView.as_view({'get': 'retrieve'}), name='usuario_logado'),
    path('register-user/', RegisterUserView.as_view(), name='register_user'),
    path('update-user/', UpdateUserView.as_view(), name='update_user'),
    path('delete-user/', DeleteUserView.as_view(), name='delete_user'),
]
