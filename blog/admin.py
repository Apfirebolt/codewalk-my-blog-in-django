from django.contrib import admin
from .models import Post, PostImages, About, Experience, PostTag, Tag


admin.site.register(Post)
admin.site.register(PostImages)
admin.site.register(About)
admin.site.register(PostTag)
admin.site.register(Tag)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'location')