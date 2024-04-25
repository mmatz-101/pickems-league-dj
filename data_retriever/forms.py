from django import forms
from .constants import LEAGUE_CHOICES


class DataRetrieverForm(forms.Form):
    league = forms.ChoiceField(choices=LEAGUE_CHOICES)
    year = forms.IntegerField(max_value=2030, min_value=2020)
    week_query = forms.IntegerField()
    week = forms.IntegerField()
