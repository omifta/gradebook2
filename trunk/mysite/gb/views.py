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

##     teachers = {}
##     for c in course_list:
##         teachers[c.id] = c.teachers.all()
##     return render_to_response('gb/allcourses.html', {'course_list': course_list,
##                                                     'teachers': teachers})
##     t = loader.get_template('gb/allcourses.html')
##     c = Context({
##         'course_list': course_list,
##     })
##     return HttpResponse(t.render(c))
##     course_list = Course.objects.all()
##     result = '<h1>List of All Courses</h1>'
##     result += '<br>'.join(['<b>%s</b> (%s)' % (c.course_name, c.section) for c in course_list])
##     return HttpResponse(result)

def teachers(request):
    """ Displays a list of all teachers.
    """
    teachers = Teacher.objects.all()
    return render_to_response('gb/allteachers.html', {'teachers' : teachers})

## def teachers(request):
##     """ Displays a list of all teachers.
##     """
##     teacher_list = Teacher.objects.all()
##     result = '<br>'.join([t.fullname() for t in teacher_list])
##     return HttpResponse(result)

def students(request):
    """ Displays a list of all teachers.
    """
    students = Student.objects.all()
    return render_to_response('gb/allstudents.html', {'students' : students})


## def students(request):
##     """ Displays a list of all students.
##     """
##     student_list = Student.objects.all()
##     result = '<br>'.join([s.fullname() for s in student_list])
##     return HttpResponse(result)

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
        #if len(courses) == 1:
        return render_to_response('gb/course.html', {'courses' : courses})
        #else:
        #    return HttpResponse('There are multiple courses with the name %s. View not yet implemented' % name)
    except:
        raise Http404
