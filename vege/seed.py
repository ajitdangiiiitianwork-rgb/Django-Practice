from logging import exception

from faker import Faker
import random
from . models import *
fake = Faker()

def seed_db(n=10) -> None:
  departments_obj = Department.objects.all()
  try:
    for _ in range(n):
      idx = random.randint(0, len(departments_obj) - 1)
      department = departments_obj[idx]
      student_id = f'STU-0{random.randint(100, 999)}'
      student_name = fake.name()
      student_age = random.randint(20, 30)
      student_email = fake.email()
      student_address = fake.address()

      student_id_obj = StudentId.objects.create(student_id = student_id)

      student_obj = Student.objects.create(
        department = department,
        student_age = student_age,
        student_email = student_email,
        student_name = student_name,
        student_address = student_address,
        student_id = student_id_obj,
      )
  except Exception as e:
    print(e)

def create_subject_marks(n):
  student_objs = Student.objects.all()
  try:
    for student in student_objs:
      subjects = Subject.objects.all()
      for subject in subjects:
        SubjectMarks.objects.create(
            student = student,
            subject = subject,
            subject_marks = random.randint(0, 100)
        )
  except Exception as e:
    print(e)
