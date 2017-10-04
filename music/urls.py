from django.conf.urls import url

# importing views for current url mappings
from . import views




urlpatterns = [

	# /music/
    url(r'^$', views.index, name='index'),
    # /music/62
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
