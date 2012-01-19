from django.contrib import admin
from skene.skenepisteet.models import Scener, ScenePointEvent

class ScenePointEventAdmin(admin.ModelAdmin):
    list_display = ('scener', 'points', 'description', 'accepted', 'award_date')
    list_filter = ('accepted',)

admin.site.register(Scener)
admin.site.register(ScenePointEvent, ScenePointEventAdmin)