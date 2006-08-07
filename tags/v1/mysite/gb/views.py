# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from mysite.gb.models import Course, Teacher, Student

def courses(request):
    """ Displays a list of all courses.
    """
    course_list = Course.objects.all()
    return render_to_response('gb/allcourses.html', {'course_list' : course_list})


def teachers(request):
    """ Displays a list of all teachers.
    """
    teachers = Teacher.objects.all()
    return render_to_response('gb/allteachers.html', {'teachers' : teachers})


def students(request):
    """ Displays a list of all teachers.
    """
    students = Student.objects.all()
    return render_to_response('gb/allstudents.html', {'students' : students})


def course(request, course_id = ''):
    try:
        all = Course.objects.all()
        c = all[course_id]
        return render_to_response('gb/course.html', {'course' : c})
    except:
        raise Http404
        

def courses_by_name(request, course_type, course_num):
    try:
        name = "%s %s" % (course_type.upper(), course_num)
        courses = Course.objects.filter(course_name = name)
        return render_to_response('gb/course.html', {'courses' : courses})
    except:
        raise Http404
