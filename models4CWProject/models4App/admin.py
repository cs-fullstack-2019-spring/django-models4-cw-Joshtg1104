from django.contrib import admin

# Register your models here.

from .models import Mom, Child

admin.site.register(Mom)
admin.site.register(Child)