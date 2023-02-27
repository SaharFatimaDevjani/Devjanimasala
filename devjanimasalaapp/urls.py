from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('', views.home),
    path('category/<int:id>', views.category),
    path('contact/', views.contact),
    path('contact/sendmail', views.sendmail),
    path('category/product/<int:id>', views.product),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]