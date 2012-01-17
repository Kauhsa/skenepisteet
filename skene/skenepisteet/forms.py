# encoding: utf-8

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from skene.skenepisteet.models import PointSuggestion

class LoginForm(forms.Form):
    username = CharField(label="Käyttäjätunnus")
    password = CharField(widget=PasswordInput, label="Salasana")

    def clean(self):
        # We will want to do this check only if form is otherwise valid - if we didn't do this, we would
        # get "Invalid username or password" even if they were empty or otherwise invalid
        if self.is_valid():
            # Check username and password - you will need to call django.contrib.auth.login() with
            # cleaned_data['user'] wherever you are using this form
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                # username or password are no longer valid - remove them from cleaned_data
                del self.cleaned_data['username']
                del self.cleaned_data['password']
                raise ValidationError("Virheellinen käyttäjätunnus tai salasana.")
            elif not user.is_active:
                del self.cleaned_data['username']
                del self.cleaned_data['password']
                raise ValidationError("Käyttäjätunnuksesi on disabloitu.")
            else:
                self.cleaned_data['user'] = user

        return self.cleaned_data

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = PointSuggestion
        exclude = ("scener", )