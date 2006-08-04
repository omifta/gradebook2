#from django.conf.urls.defaults import *
#
#urlpatterns = patterns('mysite.polls.views',
#
#    (r'^admin/', include('django.contrib.admin.urls')),
#    (r'^$', 'mysite.polls.views.index'),
#    (r'^(?P<poll_id>\d+)/$', 'detail'),
#    (r'^(?P<poll_id>\d+)/results/$', 'results'),
#    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#
#)
from django.conf.urls.defaults import *

urlpatterns = patterns('mysite.gb.views',
 (r'^allcourses/$', 'courses'),
 (r'^allteachers/$', 'teachers'),
 (r'^allstudents/$', 'students'),
 (r'^course/(?P<course_type>(macm|cmpt))(?P<course_num>\d\d\d)/$', 'courses_by_name'),
)
