from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'address', 'lat', 'lot', 'phone_number', )

admin.site.register(Post, PostAdmin)