"""firstpass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from parameters import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('parameters/',views.param_lib,name='param_lib'),
    path('parameters/new/',views.get_new_param,name='new_param'),
    path('parameters/',views.edit_param,name='edit_param'),
    path('parameters/',views.delete_param,name='delete_param'),
    path('datasources/',views.data_lib,name='data_lib'),
    path('datasources/new/',views.get_new_data,name='new_data'),
    path('datasources/',views.edit_data,name='edit_data'),
    path('datasources/',views.delete_data,name='delete_data')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
