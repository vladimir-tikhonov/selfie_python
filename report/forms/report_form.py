from django import forms

class ReportForm(forms.Form):
    reason = forms.CharField(
        label='Введите причину жалобы',
        max_length=255,
        widget=forms.Textarea
    )
