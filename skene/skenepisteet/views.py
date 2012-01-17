# encoding: utf-8
from operator import attrgetter

from django.contrib.auth import login, logout
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import simplejson
from skene.skenepisteet.forms import SuggestionForm, LoginForm
from skene.skenepisteet.models import Scener, ScenePointEvent
from djpjax import pjax
from django.contrib import messages

@pjax()
def index(request):
    # sorting manually (not with order_by) because it fails if there is no events on scener
    # as SQL backend doesn't treat NULL as 0 when sorting - we also need to manually change
    # any None in points to 0 to manual sorting to work
    sceners = list(Scener.objects.annotate(points=Sum('scenepointevent__points')))
    for scener in sceners:
        if not scener.points:
            scener.points = 0
    sceners = sorted(sceners, key=attrgetter('points'), reverse=True)

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
            return HttpResponse(simplejson.dumps({'redirect': '/', 'pjax': False}), mimetype='application/json')
    else:
        login_form = LoginForm()

    return TemplateResponse(request, "popup/login.html", {"form": login_form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Kirjauduit ulos onnistuneesti.')
    return redirect('/')