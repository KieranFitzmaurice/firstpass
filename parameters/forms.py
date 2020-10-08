from django import forms
from .models import Parameter, DataSource, Project

class NewParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ['value','input_filepath','derivation_documentation','data_source','project'] 

