from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project, Parameter, DataSource
from .forms import NewParameterForm, NewDataSourceForm
from django.utils import timezone
from .choices import get_short_code
from .filters import ParameterFilter, DataSourceFilter

# Create your views here.
def home(request):
    n_param = Parameter.objects.count()
    n_datasource = DataSource.objects.count()
    n_project = Project.objects.count()
    return render(request,'home.html',{'n_param':n_param,'n_datasource':n_datasource,'n_project':n_project})

def param_lib(request):
    params = Parameter.objects.all()
    return render(request,'param_lib.html',{'params': params})

def delete_param(request):
    params = Parameter.objects.all()
    return render(request,'param_lib.html',{'params': params})

def edit_param(request,pk):
    user = User.objects.first()
    param = get_object_or_404(Parameter, pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewParameterForm(request.POST,request.FILES,instance=param)
        # check whether it's valid:
        if form.is_valid():
            newdata = form.save(commit=False)
            newdata.modified_by = user
            newdata.modified_at = timezone.now()
            newdata.save()
            return redirect('view_param', pk=pk)
        # if a GET (or any other method) we'll create a blank form
    else:
        form = NewParameterForm(instance=param)

    return render(request, 'editparam.html', {'form': form,'param': param})

def param_add_data(request,param_pk):
    param = get_object_or_404(Parameter,pk=param_pk)
    datasources = DataSource.objects.exclude(pk__in=param.data_sources.all().values_list('pk', flat=True))
    datafilter = DataSourceFilter(request.GET, queryset=datasources)
    return render(request,'param_add_data.html',{'datafilter': datafilter,'param': param})

def param_link_data(request,param_pk,data_pk):
    user = User.objects.first()
    param=get_object_or_404(Parameter,pk=param_pk)
    datasource=get_object_or_404(DataSource,pk=data_pk)
    datasource.parameters.add(param)
    param.data_sources.add(datasource)
    datasource.modified_by = user
    datasource.modified_at = timezone.now()
    param.modified_by = user
    param.modified_at = timezone.now()
    datasource.save()
    param.save()
    return redirect('param_add_data', param_pk=param_pk)

def unlink_data_from_param(request,param_pk,data_pk):
    user = User.objects.first()
    datasource = get_object_or_404(DataSource,pk=data_pk)
    param = get_object_or_404(Parameter,pk=param_pk)
    datasource.parameters.remove(param)
    param.data_sources.remove(datasource)
    datasource.modified_by = user
    datasource.modified_at = timezone.now()
    param.modified_by = user
    param.modified_at = timezone.now()
    datasource.save()
    param.save()
    return redirect('view_param', pk=param_pk)

def view_param(request,pk):
    param = get_object_or_404(Parameter, pk=pk)
    return render(request,'view_param.html',{'param':param})

def get_new_param(request):
    user = User.objects.first()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewParameterForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            newparam = form.save(commit=False)
            newparam.created_by = user
            newparam.created_at = timezone.now()
            newparam.modified_by = user
            newparam.modified_at = user
            newparam.save()
            return redirect('view_param',pk=newparam.pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewParameterForm()

    return render(request, 'newparameter.html', {'form': form})

def data_new_param(request,data_pk):
    user = User.objects.first()
    datasource = get_object_or_404(DataSource, pk=data_pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewParameterForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            newparam = form.save(commit=False)
            newparam.created_by = user
            newparam.created_at = timezone.now()
            newparam.modified_by = user
            newparam.modified_at = timezone.now()
            newparam.save()
            datasource.parameters.add(newparam)
            newparam.data_sources.add(datasource)
            datasource.modified_by = user
            datasource.modified_at = timezone.now()
            datasource.save()
            newparam.save()
            return redirect('view_data',pk=data_pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewParameterForm()

    return render(request, 'newparameter.html', {'form': form})

def data_lib(request):
    datasources = DataSource.objects.all()
    datafilter = DataSourceFilter(request.GET, queryset=datasources)
    return render(request,'data_lib.html',{'datafilter':datafilter})

def delete_data(request):
    datasources = DataSource.objects.all()
    return render(request,'data_lib.html',{'datasources': datasources})

def view_data(request,pk):
    datasource = get_object_or_404(DataSource, pk=pk)
    return render(request,'view_data.html',{'datasource':datasource})

def get_new_data(request):
    user = User.objects.first()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewDataSourceForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            newdata = form.save(commit=False)
            newdata.created_by = user
            newdata.created_at = timezone.now()
            newdata.modified_by = user
            newdata.modified_at = timezone.now()
            newdata.CountryCode = get_short_code(newdata.Country)
            newdata.save()
            return redirect('view_data',pk=newdata.pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewDataSourceForm()

    return render(request, 'newdata.html', {'form': form})

def param_new_data(request,param_pk):
    user = User.objects.first()
    param = get_object_or_404(Parameter, pk=param_pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewDataSourceForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            newdata = form.save(commit=False)
            newdata.created_by = user
            newdata.created_at = timezone.now()
            newdata.modified_by = user
            newdata.modified_at = timezone.now()
            newdata.CountryCode = get_short_code(newdata.Country)
            newdata.save()
            newdata.parameters.add(param)
            param.data_sources.add(newdata)
            param.modified_by = user
            param.modified_at = timezone.now()
            param.save()
            newdata.save()
            return redirect('view_param',pk=param_pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewDataSourceForm()

    return render(request, 'newdata.html', {'form': form})

def edit_data(request,pk):
    user = User.objects.first()
    datasource = get_object_or_404(DataSource, pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewDataSourceForm(request.POST,request.FILES,instance=datasource)
        # check whether it's valid:
        if form.is_valid():
            newdata = form.save(commit=False)
            newdata.modified_by = user
            newdata.modified_at = timezone.now()
            newdata.CountryCode = get_short_code(newdata.Country)
            newdata.save()
            return redirect('view_data', pk=pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewDataSourceForm(instance=datasource)

    return render(request, 'editdata.html', {'form': form,'datasource': datasource})

def data_add_param(request,data_pk):
    datasource = get_object_or_404(DataSource,pk=data_pk)
    params = Parameter.objects.exclude(pk__in=datasource.parameters.all().values_list('pk', flat=True))
    return render(request,'data_add_param.html',{'params': params,'datasource': datasource})

def data_link_param(request,data_pk,param_pk):
    user = User.objects.first()
    param=get_object_or_404(Parameter,pk=param_pk)
    datasource=get_object_or_404(DataSource,pk=data_pk)
    datasource.parameters.add(param)
    param.data_sources.add(datasource)
    datasource.modified_by = user
    datasource.modified_at = timezone.now()
    param.modified_by = user
    param.modified_at = timezone.now()
    datasource.save()
    param.save()
    return redirect('data_add_param', data_pk=data_pk)

def unlink_param_from_data(request,data_pk,param_pk):
    user = User.objects.first()
    datasource = get_object_or_404(DataSource,pk=data_pk)
    param = get_object_or_404(Parameter,pk=param_pk)
    datasource.parameters.remove(param)
    param.data_sources.remove(datasource)
    datasource.modified_by = user
    datasource.modified_at = timezone.now()
    param.modified_by = user
    param.modified_at = timezone.now()
    datasource.save()
    param.save()
    return redirect('view_data', pk=data_pk)
