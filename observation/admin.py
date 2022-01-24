from django.contrib import admin

# Register your models here.
from observation.models import InfoField
from observation.models import InfoLine
admin.site.register(InfoField)
admin.site.register(InfoLine)