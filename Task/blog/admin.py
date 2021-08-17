from django.contrib import admin
from modeltranslation.admin import TranslationAdmin ,TranslationTabularInline
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
# Register your models here.
# admin.site.register(Post, PostAdmin)

class PosttrAdmin(TranslationAdmin):
    model = Post

#class BlogAdminArea(admin.AdminSite):
#    site_header = "Please Log in"

#blog_admin = BlogAdminArea(name="BlogAdmin")


admin.site.register(Post, PostAdmin)