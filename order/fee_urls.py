from django.conf.urls import patterns, include, url

urlpatterns = patterns('order.views',
    # Examples:
    url(r'create/$', 'create_fee', name='create_fee'),
    url(r'^(?P<fee_id>\d+)$','fee_restful', name="fee_restful"),
    )
