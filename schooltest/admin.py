from django.contrib import admin

# Register your models here.
from .models import Result, Question, Answer,Quiz

class QuizesAdmin(admin.ModelAdmin):
  
  list_display = ['name','topic','number_of_questions','difficulty','time']
  list_filter = ['name','topic','difficulty']
  list_editable = ['topic','number_of_questions','time'] #####ห้ามมีตัวแรกคือ'username


class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class ShowAdmin(admin.ModelAdmin):
  
  list_display = ['question','text','correct','created']
  list_filter = ['question','created']
  list_editable = ['correct'] #####ห้ามมีตัวแรกคือ'username
  
class ShowresultAdmin(admin.ModelAdmin):
  
  list_display = ['user','quiz','score','created']
  list_filter = ['user','quiz']
  # list_editable = ['created'] #####ห้ามมีตัวแรกคือ'username
  
admin.site.register(Quiz, QuizesAdmin)   