from django import forms

class PaymentForm(forms.Form):
    identity = forms.CharField(
        label='Имя на карте',
    )
    card = forms.CharField(
        label='Номер карты',
    )
    cvv = forms.CharField(
        label='cvv',
    )
