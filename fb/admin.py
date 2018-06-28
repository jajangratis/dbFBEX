from django.contrib import admin
from .models import Timeline , Comments , Notifications ,Members
# Register your models here.


admin.site.register (Timeline),
admin.site.register (Comments),
admin.site.register (Notifications),
admin.site.register (Members),