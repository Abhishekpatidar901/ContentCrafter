from django.contrib import admin

# Register your models here.
from .models import List, Subscriber, Email


admin.site.register(List)
admin.site.register(Subscriber)
admin.site.register(Email)