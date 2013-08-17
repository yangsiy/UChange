from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uchange.views.home', name='home'),
    # url(r'^uchange/', include('uchange.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/',include('uchange_app.urls', namespace='user')),
    url(r'^$', 'uchange.views.index', name='index'),
    url(r'^login/$','uchange.views.user_login', name='user_login'),
    url(r'^logout/$','uchange.views.user_logout', name='user_logout'),
    url(r'^register/$','uchange.views.register', name='register'),
    url(r'^register/operate/$','uchange.views.register_operate', name='register_operate'),
)
