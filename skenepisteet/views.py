# encoding: utf-8
from django.contrib.auth import login

from django.db.models import Sum
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import simplejson
from skenepisteet.forms import SuggestionForm, LoginForm
from skenepisteet.models import Scener, ScenePointEvent
from djpjax import pjax
from django.contrib import messages

@pjax()
def index(request):
    sceners = Scener.objects.annotate(points=Sum('scenepointevent__points')).order_by('-points')
    activity = ScenePointEvent.objects.order_by('-award_date')[:5]
    return TemplateResponse(request, "index.html", {"sceners": sceners, "activities": activity})

def info_popup(request, scener_id=None):
    scener = Scener.objects.annotate(points=Sum('scenepointevent__points')).get(id=scener_id)

    if request.method == "POST":
        suggestion_form = SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.scener = scener
            suggestion.save()
            messages.info(request, u'Pistemuutosehdotuksesi henkilöä "%s" kohtaan on otettu vastaan. Kiitos!' % scener.name)
            return HttpResponse(simplejson.dumps({'redirect': '/'}), mimetype='application/json')
    else:
        suggestion_form = SuggestionForm()

    return TemplateResponse(request, "popup/user_suggest.html", {"scener": scener, "form": suggestion_form})

def login_popup(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data.get('user')
            login(request, user)
            messages.info(request, u'Sisäänkirjautuminen onnistui.')
            return HttpResponse(simplejson.dumps({'redirect': '/'}), mimetype='application/json')
    else:
        login_form = LoginForm()

    return TemplateResponse(request, "popup/login.html", {"form": login_form})