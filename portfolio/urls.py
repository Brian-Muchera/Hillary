from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='portfolio'
urlpatterns = [
    #index function
    path('', views.index, name='index'),
    #ajax functon
    path('ajax/inquiry/', views.inquiry, name='inquiry'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
