from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse

from . import models


class ConcertAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect(reverse('concert_detail', args=[str(obj.pk)]))

    def response_change(self, request, obj):
        return redirect(reverse('concert_detail', args=[str(obj.pk)]))


admin.site.register(models.Band)
admin.site.register(models.City)
admin.site.register(models.Concert, ConcertAdmin)
