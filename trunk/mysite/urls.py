from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^polls/', include('mysite.polls.urls')),
    (r'^gb/', include('mysite.gb.urls'))                   
)

## urlpatterns = patterns('',
##     # Example:
##     # (r'^mysite/', include('mysite.apps.foo.urls.foo')),

##     # Uncomment this for admin:
     
##     (r'^admin/', include('django.contrib.admin.urls')),
##     (r'^polls/', include('mysite.polls.urls')),
##     (r'^gb/', include('mysite.gb.urls'))                   
##     #(r'^polls/$', 'mysite.polls.views.index'),
##     #(r'^polls/(?P<poll_id>\d+)/$', 'mysite.polls.views.detail'),
##     #(r'^polls/(?P<poll_id>\d+)/results/$', 'mysite.polls.views.results'),
##     #(r'^polls/(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),

## )
