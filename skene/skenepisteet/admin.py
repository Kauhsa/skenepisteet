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

admin.site.register(Scener, ScenerAdmin)
admin.site.register(ScenePointEvent, ScenePointEventAdmin)