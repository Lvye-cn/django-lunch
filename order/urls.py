from django.conf.urls import patterns, include, url

urlpatterns = patterns('order.views',
    # Examples:
    url(r'create/$', 'create_order', name='create_order'),
    # url(r'^blog/', include('blog.urls')),

    )
