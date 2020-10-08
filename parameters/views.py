from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project, Parameter, DataSource
from .forms import NewParameterForm, NewDataSourceForm

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

def edit_param(request):
    params = Parameter.objects.all()
    return render(request,'param_lib.html',{'params': params})

def get_new_param(request):
    user = User.objects.first()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewParameterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newparam = form.save(commit=False)
            newparam.created_by = user
            newparam.save()
            return redirect('param_lib')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewParameterForm()

    return render(request, 'newparameter.html', {'form': form})

def data_lib(request):
    datasources = DataSource.objects.all()
    return render(request,'data_lib.html',{'datasources': datasources})

def delete_data(request):
    datasources = DataSource.objects.all()
    return render(request,'data_lib.html',{'datasources': datasources})

def edit_data(request):
    datasources = DataSource.objects.all()
    return render(request,'data_lib.html',{'datasources': datasources})

def get_new_data(request):
    user = User.objects.first()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewDataSourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newdata = form.save(commit=False)
            newdata.save()
            return redirect('data_lib')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewDataSourceForm()

    return render(request, 'newdata.html', {'form': form})
