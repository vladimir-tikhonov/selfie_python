from django import forms
import html5.forms.widgets as html5_widgets

class ReportParamsForm(forms.Form):
    start = forms.DateField(label="Дата начала", widget=html5_widgets.DateInput)
    end = forms.DateField(label="Дата окончания", widget=html5_widgets.DateInput)
