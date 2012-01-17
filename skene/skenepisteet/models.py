# encoding: utf-8

from django.db import models

class Scener(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name

class ScenePointEvent(models.Model):
    points = models.IntegerField(help_text=u"Negatiivinen luku, jos haluat vähentää henkilöltä pisteitä.", verbose_name=u"Pisteet")
    description = models.TextField(help_text=u"Perustelut, miksi henkilön pisteitä pitäisi muuttaa.", verbose_name=u"Perustelut")
    award_date = models.DateTimeField(auto_created=True)
    scener = models.ForeignKey(Scener)
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.description

class PointSuggestion(models.Model):
    scener = models.ForeignKey(Scener)
    points = models.IntegerField(help_text=u"Anna negatiivinen luku, jos haluat vähentää henkilöltä pisteitä.", verbose_name=u"Pisteet")
    reason = models.TextField(help_text=u"Kirjoita tähän perustelut, miksi henkilön pisteitä pitäisi muuttaa.", verbose_name=u"Perustelut")

    def __unicode__(self):
        return self.reason
