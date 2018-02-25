from django.contrib import admin
from .models import Palier,Module,Course,Tutorial
from videos.models import Video
# Register your models here.

class TutorialInline(admin.TabularInline):
    model = Tutorial
    fields = ('title','video','quiz')

class CourseAdmin(admin.ModelAdmin):
    inlines = [TutorialInline]


admin.site.register(Palier)
admin.site.register(Module)
admin.site.register(Course,CourseAdmin)
