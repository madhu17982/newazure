from django.contrib import admin
from .models import rack_Azure


class djangoadmin(admin.ModelAdmin):
    list_display=['subject','explanation']
admin.site.register(rack_Azure,djangoadmin)








