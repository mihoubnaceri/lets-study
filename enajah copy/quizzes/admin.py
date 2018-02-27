from django.contrib import admin
from .models import Quiz,Question,Indice,Answer
# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question
    fields = ("order","question_type","question_text",)

class IndiceInline(admin.TabularInline):
    model = Indice
    fields = ("indice_text",)
    extra=3

class AnswerInline(admin.TabularInline):
    model=Answer
    fields = ("answer_text","correct",)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,IndiceInline]
class QuizAdmin(admin.ModelAdmin):
    inlines=[QuestionInline]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz,QuizAdmin)
