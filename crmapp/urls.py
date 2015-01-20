from django.conf.urls import patterns, include, url

from marketing.views import HomePage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',HomePage.as_view(),name="Home")
    # url(r'^contact-us/(?P<lang>[\w-])/$',ContactUs.asview())
)
