# encoding: utf-8
from django.contrib import admin
from skene.skenepisteet.models import Scener, ScenePointEvent

class InlineScenePointEvent(admin.TabularInline):
    model = ScenePointEvent
    extra = 0

class ScenerAdmin(admin.ModelAdmin):
    inlines = (InlineScenePointEvent,)

class ScenePointEventAdmin(admin.ModelAdmin):
    list_display = ('scener', 'points', 'description', 'accepted', 'award_date')
    list_filter = ('accepted',)
    actions = ('set_accepted',)

    def set_accepted(self, request, queryset):
        queryset.update(accepted=True)
    set_accepted.short_description = u"Merkitse hyväksytyiksi"

admin.site.register(Scener, ScenerAdmin)
admin.site.register(ScenePointEvent, ScenePointEventAdmin)