# encoding: utf-8
from operator import attrgetter

from django.db.models import Sum
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import simplejson
from skene.skenepisteet.forms import SuggestionForm
from skene.skenepisteet.models import Scener, ScenePointEvent
from djpjax import pjax
from django.contrib import messages

@pjax()
def index(request):
    # sorting manually (not with order_by) because it fails if there is no events on scener
    # as SQL backend doesn't treat NULL as 0 when sorting - we also need to manually change
    # any None in points to 0 to manual sorting to work
    sceners = Scener.objects.filter(scenepointevent__accepted=True).annotate(points=Sum('scenepointevent__points'))
    sceners = list(sceners)
    for scener in sceners:
        if not scener.points:
            scener.points = 0
    sceners = sorted(sceners, key=attrgetter('points'), reverse=True)

    activity = ScenePointEvent.objects.filter(accepted=True).order_by('-award_date')[:5]
    return TemplateResponse(request, "index.html", {"sceners": sceners, "activities": activity})

def info_popup(request, scener_id=None):
    scener = Scener.objects.filter(scenepointevent__accepted=True).annotate(points=Sum('scenepointevent__points')).get(id=scener_id)

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