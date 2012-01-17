# encoding: utf-8

from django import forms
from skene.skenepisteet.models import ScenePointEvent

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = ScenePointEvent
        exclude = ("scener", "accepted", "award_date")