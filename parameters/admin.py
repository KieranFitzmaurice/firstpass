from django.contrib import admin
from .models import Project,Parameter,DataSource,InFile

# Register your models here.

admin.site.register(Project)
admin.site.register(Parameter)
admin.site.register(DataSource)
admin.site.register(InFile)
