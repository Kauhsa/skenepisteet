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
    # TODO: Check how many queries this really does
    # get sceners with points - this returns only sceners that have any events associated on them, which is why we have
    # to do this on two separate queries
    scener_points = Scener.objects.filter(scenepointevent__accepted=True).annotate(points=Sum('scenepointevent__points'))

    # get all sceners we want to show on front page
    sceners = Scener.objects.all()

    # add points to scener
    for scener in sceners:
        if scener_points.filter(id = scener.id):
            scener.points = scener_points.get(id = scener.id).points
        else:
            scener.points = 0

    # sort sceners according to their points
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