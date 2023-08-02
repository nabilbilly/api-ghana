from django.contrib import admin
from .models import Posts
# Register your models here.


# admin.site.register(Posts)
#how to get entity types displayed in the admin area "register"
@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('regions', 'districts')
    ordering = ('regions',)
    search_fields = ('regions',)