from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User

class RegistrationForm(UserCreationForm):
    is_vip = forms.BooleanField(
        label='Хотите зарегистрироваться как vip-пользователь?',
        required=False
    )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if self.cleaned_data['is_vip']:
            user.is_active=False
            user.role=1
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", )
