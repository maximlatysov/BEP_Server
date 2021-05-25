from django.contrib import admin
from .models import Appdata
from .models import Localization

admin.site.register(Appdata)
admin.site.register(Localization)