from django.contrib import admin

from . import models


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'author', 'created_date',)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
