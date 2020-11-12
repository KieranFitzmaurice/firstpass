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
    path('parameters/<int:pk>/',views.view_param,name='view_param'),
    path('parameters/<int:param_pk>/new-data/',views.param_new_data,name='param_new_data'),
    path('parameters/<int:param_pk>/add-data/',views.param_add_data,name='param_add_data'),
    path('parameters/<int:pk>/edit/',views.edit_param,name='edit_param'),
    path('parameters/<int:param_pk>/add-data/<int:data_pk>/',views.param_link_data,name='param_link_data'),
    path('parameters/<int:param_pk>/unlink/<int:data_pk>/',views.unlink_data_from_param,name='unlink_data_from_param'),
    path('parameters/',views.delete_param,name='delete_param'),
    path('datasources/',views.data_lib,name='data_lib'),
    path('datasources/new/',views.get_new_data,name='new_data'),
    path('datasources/<int:pk>/',views.view_data,name='view_data'),
    path('datasources/<int:data_pk>/new-param/',views.data_new_param,name='data_new_param'),
    path('datasources/<int:data_pk>/add-param/',views.data_add_param,name='data_add_param'),
    path('datasources/<int:pk>/edit/',views.edit_data,name='edit_data'),
    path('datasources/<int:data_pk>/add-param/<int:param_pk>/',views.data_link_param,name='data_link_param'),
    path('datasources/<int:data_pk>/unlink/<int:param_pk>/',views.unlink_param_from_data,name='unlink_param_from_data'),
    path('datasources/',views.delete_data,name='delete_data'),
    path('inputfiles/',views.test_infile,name='test_infile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
