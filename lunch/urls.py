from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lunch.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logout/$', 'lunch.views.logout_user', name='logout'),
    url(r'^login/$', 'lunch.views.login_user', name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^order/', include('order.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
