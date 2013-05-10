from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'livehouse.views.mainpage'),
    url(r'^teacher$', 'livehouse.views.teacher'),
    url(r'^course$', 'livehouse.views.course'),
    url(r'^course/(?P<cid>\d+)/$', 'livehouse.views.one_course'),
    url(r'^teacher/(?P<tid>\d+)/$', 'livehouse.views.one_teacher'),
    url(r'^mycourse$', 'livehouse.views.mycourse'),
    url(r'^setupclass$', 'livehouse.views.setupclass'),
    url(r'^reg$', 'livehouse.views.reg'),
    url(r'^login$', 'livehouse.views.login'),
    url(r'^logout$', 'livehouse.views.logout'),
    # url(r'^livehouse/', include('livehouse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
