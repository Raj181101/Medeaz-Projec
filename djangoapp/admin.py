from django.contrib import admin
from djangoapp.models import user
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=['user','father','mother','brother','sister']

admin.site.register(user,useradmin)