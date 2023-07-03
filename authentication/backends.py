from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from phonenumbers import parse, is_valid_number


class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)  # Check if the username is an email
        except User.DoesNotExist:
            if is_valid_number(parse(username, None)):
                try:
                    user = User.objects.get(phone_number=username)  # Check if the username is a phone number
                except User.DoesNotExist:
                    return None
            else:
                return None
        if user.check_password(password):
            return user
        return None
