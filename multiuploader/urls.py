from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^multiuploader_delete_multiple/$', multiuploader_delete_multiple,
        name='multiuploader_delete_multiple'),
    url(r'^multiuploader_delete/(?P<pk>\w+)/$', multiuploader_delete,
        name='multiuploader_delete'),
    url(r'^multiuploader/$', multiuploader,
        name='multiuploader'),
    url(r'^multiuploader_noajax/$', multiuploader, kwargs={"noajax": True},
        name='multiploader_noajax'),
    url(r'^multiuploader_file/(?P<pk>\w*)/$', multi_show_uploaded,
        name='multiuploader_file_link')
]
