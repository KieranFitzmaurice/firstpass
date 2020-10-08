from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project, Parameter, DataSource
from .forms import NewParameterForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def param_lib(request):
    params = Parameter.objects.all()
    return render(request,'param_lib.html',{'params': params})

#def section_topics(request,section_id):
#    section = get_object_or_404(Section,id=section_id)
#    return render(request,'sections.html',{'section': section})

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
