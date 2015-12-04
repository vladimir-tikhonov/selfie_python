from django import forms

class PostForm(forms.Form):
    picture = forms.FileField(
        label='Выберите изображение'
    )
