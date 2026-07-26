from django.contrib import admin
from django.db.models import Sum 

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


class ReportCardAdmin(admin.ModelAdmin):
  list_display = ['student', 'total_marks' ,'student_rank', 'date_of_report_card_generation']
  ordering = ['student_rank']
  def total_marks(self, obj):
    subject_marks = SubjectMarks.objects.filter(student = obj.student)
    return subject_marks.aggregate(subject_marks =  Sum('subject_marks'))['subject_marks']
admin.site.register(ReportCard, ReportCardAdmin)
