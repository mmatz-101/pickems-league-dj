from django import forms

class DataRetrieverForm(forms.Form):
    CHOICES = [
        ("nfl", "NFL"),
        ("ncaa", "NCAA")
    ]
    league = forms.CharField()
    year = forms.IntegerField(max_value=2030, min_value=2020)
    week = forms.IntegerField()

