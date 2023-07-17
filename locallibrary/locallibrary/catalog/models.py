from django.db import models
from django.urls import reverse
import Classroom, Details_Semester, course, Details_Health

class Classroom(models.Model):
 	student = models.ForingKey(Student,student_id)
 	teacher = models.ForingKey(Teacher,teacher_id)
 	course = models.ForingKey(Course,course_id)
 	capacidad = models.IntegerField()
 	Num_Classroom = models.CharField(max_length=255)
 	Classroom_active = models.BooleanField(default=True)    
	 
 	class Meta:
	    verbose_name_plural = 'Classroom'
	    ordering = ('-created',)
 	def __str__(self):
		 return self.title
	

class Details_Semester(models.Model):
   semester_id = models.CharField(max_length=200)
   plan_id=models.CharField(max_length=200)
   falculty_id=models.CharField(max_length=200)
   semesterName=models.CharField(max_length=255)
   semesterStatus=models.BooleanField(default=True)


   planStatus=models.BooleanField(default=True)
   planYear= models.CharField(max_length=255)
   faculty_name=models.CharFiel(max_length=200)




   def __str__(self):       """Returns the URL to access a detail record for this book."""
       return reverse('book-detail', args=[str(self.id)])


class course(models.MOdel):
   status=models.BooleanField(default=True)
   organizationId=models.CharFiel(max_length=200)


   organizationConect = models.ManyToManyField(organization, help_text='detalle relacion con organizacion')


   def __str__(self):
       """String for representing the Model object."""
       return self.title

class Details_Health(models.Model):
   name=models.CharFiel(max_length=200)
   typeBlood=models.CharFiel(max_length=200)


   studentRelation = models.ManyToManyField(teacher, help_text='Select a genre for this book')
   TeacherRelation = models.ManyToManyField(student, help_text='Select a genre for this book')


   def __str__(self):       """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])