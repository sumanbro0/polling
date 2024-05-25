from django.contrib import admin
from .models import Poll, Question, Submission
from django.contrib import admin
from .models import Poll, Question, Submission,Profile

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of extra forms displayed

class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer')

admin.site.register(Poll, PollAdmin)
admin.site.register(Profile)