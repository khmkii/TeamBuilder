from django.contrib import admin

from . import models


admin.site.register(models.SiteUser)
admin.site .register(models.Profile)