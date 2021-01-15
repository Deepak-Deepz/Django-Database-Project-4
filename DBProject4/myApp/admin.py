from django.contrib import admin
from myApp.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    l = ['loaction', 'lastdate', 'sal','discri']


admin.site.register(Job,JobAdmin)