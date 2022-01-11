from django.contrib import admin
from .models import *
# Register your models here.

# list of models to be displayed in the admin page
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','date','time','description')

class PujaAdmin(admin.ModelAdmin):
    list_display = ('title','category','start_date','end_date','description','image')

admin.site.register(News, NewsAdmin)
admin.site.register(Events, EventAdmin)
admin.site.register(Pujas, PujaAdmin)
