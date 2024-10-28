#Local Imports
from account.models import User

from rest_framework_simplejwt.tokens import RefreshToken


def get_user_by_email(email):
  users = User.objects.filter(email=email)
  if users.exists():
    return users.first()
  return None


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  access = refresh.access_token

  access['name'] = user.name
  access['email'] = user.email
  access['is_admin'] = user.is_admin

  return {
    'refresh': str(refresh),
    'access': str(access),
  }
