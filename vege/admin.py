from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(Recipe)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
  list_display = ['student', 'subject', 'subject_marks']

admin.site.register(SubjectMarks, SubjectMarkAdmin)