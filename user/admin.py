from django.contrib import admin

from user.models import Participant

# Register your models here.
class AdminParticipant(admin.ModelAdmin):
    list_display = ('first_name','last_name','number', 'email')
    search_fields = ('first_name','last_name','number', 'email')
    ordering = ('first_name','last_name','number', 'email')
    filter = ('first_name','last_name','number', 'email')
    list_filter = ('first_name','last_name','number', 'email')


admin.site.register(Participant, AdminParticipant)