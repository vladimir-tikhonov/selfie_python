from django import forms

class ClaimForm(forms.Form):
    reason = forms.CharField(
        label='Введите причину жалобы',
        max_length=255,
        widget=forms.Textarea
    )
