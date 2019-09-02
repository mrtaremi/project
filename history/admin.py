from django.contrib import admin

from history.models import State, Place, Category, PlaceImage
from django.contrib.auth.admin import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


class StateAdmin(admin.ModelAdmin):
    search_fields = ['name', ]


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name','category','state',)
    search_fields = ['name','category',]
    list_filter = ('category','state')
    autocomplete_fields = ['state']


admin.site.register(Category)
admin.site.register(State, StateAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)