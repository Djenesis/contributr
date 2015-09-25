from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created_date',)


admin.site.register(Post, PostAdmin)
