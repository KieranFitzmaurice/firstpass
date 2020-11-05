from django import forms
from .models import Parameter, DataSource, Project
from .choices import country_options, publication_options, parameter_options, parameter_pretty_options, status_options

class NewParameterForm(forms.ModelForm):
    PRETTY_TYPE_CHOICES = parameter_pretty_options()
    type = forms.ChoiceField(choices=PRETTY_TYPE_CHOICES,initial='Numeric value',required=True,label="Type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text
        if self.instance:
            self.fields['type'].initial = self.instance.type

    class Meta:
        model = Parameter
        fields = ['value','type','input_filepath','derivation_documentation','status','notes']

class NewDataSourceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text

    class Meta:
        model = DataSource
        fields = ['PubType','Author','Title','Date_published','Country','URL','DOI','PMID','hard_copy','notes']
