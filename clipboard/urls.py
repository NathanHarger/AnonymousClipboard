from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	
   
	url(r'^clipboard/$', views.EntryList.as_view()),
    #url(r'^clipboard/(?P<session_id>[a-zA-Z0-9]+)/(?P<media_type>[0,1]{1})/$', views.EntryDetail.as_view()),
    url(r'^clipboard/(?P<session_id>[a-zA-Z0-9]+)/$', views.EntryDetail.as_view()),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
