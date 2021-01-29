from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.HomeView, name='home'),
    path('getstream', views.index, name='streamdt'),
    path('stream', views.StreamView, name='streamroom'),
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)