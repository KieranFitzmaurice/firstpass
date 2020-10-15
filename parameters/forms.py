from django import forms
from .models import Parameter, DataSource, Project

class NewParameterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text

    class Meta:
        model = Parameter
        fields = ['value','input_filepath','derivation_documentation','notes']

class NewDataSourceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text

    class Meta:
        model = DataSource
        fields = ['PubType','Author','Title','Date_published','Country','URL','DOI','PMID','hard_copy','notes']
