from django.contrib.auth.forms import UserCreationForm
from user.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", )
