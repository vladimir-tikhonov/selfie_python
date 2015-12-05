from django import forms

class VoteForm(forms.Form):
    value = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)], required=True)
