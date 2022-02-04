from django.contrib import admin
from hack.models import BaseModel

# Register your models here.
@admin.register(BaseModel)

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'by', 'type')

    list_filter = ('type',)

    search_fields = ('title', 'body',)

    ordering = ('by',)
