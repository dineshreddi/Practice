from django.conf.urls import url, patterns

from django.contrib import admin
from djangoapp import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoprj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.djangopage),
    url(r'^login/', views.load_login),
    url(r'^register/', views.load_register),
    url(r'^show_details/', views.show_details),
    url(r'^do_reg/', views.do_registration),
)
