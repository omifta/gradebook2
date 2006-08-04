from django.db import models
import datetime


class Teacher(models.Model):
    sfu_id = models.CharField(maxlength = 9, core = True, primary_key = True)
    first_name = models.CharField(maxlength = 20, core = True)
    last_name = models.CharField(maxlength = 20, core = True)
    sfu_email = models.EmailField(core = True, unique = True)
    #contact info?

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def courses_taught(self):
        return self.course_set.all()
    
    def __str__(self):
        return self.fullname()

    class Admin: pass
    class Meta:
        ordering = ['last_name', 'first_name']
        
class Student(models.Model):
    sfu_id = models.CharField(maxlength = 9, core = True, primary_key = True)
    first_name = models.CharField(maxlength = 20, core = True)
    last_name = models.CharField(maxlength = 20, core = True)
    sfu_email = models.EmailField(core = True, unique = True)

    # helper methods
    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def courses_taken(self):
        return self.course_set.all()

    def __str__(self):
        return self.fullname()

    # the Admin class is needed to instantate the adminstration pages for this class;
    # many configuration options exist, although the default works well
    class Admin: pass

    # Meta information about the table; the "ordering" variable gives a default
    # ordering for the rows of data, i.e. in ascending order by last_name, and then
    # by first_name
    class Meta:
        ordering = ['last_name', 'first_name']
    
class Course(models.Model):
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)
    course_name = models.CharField(maxlength = 100, core = True)
    course_year = models.CharField(maxlength = 4, core = True)
    section = models.CharField(maxlength = 4, core = True)
    SEMESTER_CHOICES = (
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall')
        )
    semester = models.CharField(maxlength = 10, choices = SEMESTER_CHOICES, default = 'fall')

    def taught_by(self):
        return self.teachers.all()

    def taken_by(self):
        return self.students.all()

    def activities(self):
        return self.activity_set.all()
    
    def __str__(self):
        return self.course_name
    
    class Admin: pass
    class Meta:
        ordering = ['course_year', 'course_name']
    
class Activity(models.Model):
    # one Course can have multiple activities    
    course = models.ForeignKey(Course, edit_inline = models.STACKED, num_in_admin = 1) 
    activity_name = models.CharField(maxlength = 100, core = True)
    description = models.TextField()
    assessed = models.BooleanField(default = True)
    due_date = models.DateTimeField('due date')
    out_of = models.PositiveIntegerField(default = 100)
    weight = models.PositiveIntegerField()
    ACTIVITY_TYPE_CHOICES = (
        ('exam', 'Exam'),
        ('assignment', 'Assignment'),
        ('lab', 'Lab'),
        ('other', 'Other')
        ) 
    activity_type = models.CharField(maxlength = 10, choices = ACTIVITY_TYPE_CHOICES)
    
    def __str__(self):
        return self.activity_name

    def past_due(self):
        return self.due_date < self.due_date.now()

    class Admin: pass
    class Meta:
        ordering = ['course', 'due_date']
        verbose_name_plural = "Activities"


class StudentActivity(models.Model):
    student = models.ForeignKey(Student)   # one Student does many StudentActivities
    activity = models.ForeignKey(Activity) # one Activity is done by many students
    #marked_by = models.ForeignKey(Teacher) # one Teacher markes many StudentActivities

    submitted = models.BooleanField(default = False)
    marked = models.BooleanField(default = False)
    date_submitted = models.DateTimeField('date submitted')
    assigned_mark = models.IntegerField()  # numeric only: how to allow letter grades, etc.?

    marker_comment = models.TextField(default = '--- marker has not written a comment ---')
    def __str__(self):
        return self.activity.course.course_name

    class Admin:
        list_display = ('student', 'activity')
    class Meta:
        verbose_name_plural = "Student Activities"
