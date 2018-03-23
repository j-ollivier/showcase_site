from django.contrib import admin
from .models import *

#####################################################################
class AdminContactMessage(admin.ModelAdmin):
    list_display= ['uid', 'nom', 'contenu', 'remote_addr']
    ordering= ['nom']
admin.site.register(ContactMessage, AdminContactMessage)