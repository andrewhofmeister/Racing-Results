from django.contrib import admin

from .models import Round
from fetch.models import Races

admin.site.register(Round)
admin.site.register(Races)