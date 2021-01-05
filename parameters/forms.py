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

class EditJSONForm(forms.Form):
    # number string boolean list null

    def __init__(self, fieldlist, *args, **kwargs):
        super(EditJSONForm, self).__init__(*args, **kwargs)
        # Construct an arbitrary form based on the infile model's fieldlist field
        #fieldlist = kwargs.pop('fieldlist')
        klist = list(fieldlist.keys())
        for k in klist:
            if fieldlist[k]['data_type'] == 'number':
                self.fields[k] = forms.FloatField(widget=forms.NumberInput(attrs={'class':'custom-number-input'}))
                self.fields[k].initial = fieldlist[k]['initial']

            elif fieldlist[k]['data_type'] == 'string':
                self.fields[k] = forms.CharField(widget=forms.TextInput(attrs={'class':'custom-string-input'}))
                self.fields[k].initial = fieldlist[k]['initial']

            elif fieldlist[k]['data_type'] == 'boolean':
                self.fields[k] = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'custom-boolean-input'}),
                choices=[(True, 'True'),(False, 'False')])
                self.fields[k].initial = fieldlist[k]['initial']


            # Haven't fully worked things out for lists and nulls yet
            elif fieldlist[k]['data_type'] == 'list':
                self.fields[k] = forms.CharField(widget=forms.TextInput(attrs={'class':'custom-string-input'}))
                self.fields[k].initial = str(fieldlist[k]['initial'])

            else: # null value
                self.fields[k] = forms.CharField(widget=forms.TextInput(attrs={'class':'custom-string-input'}))
                self.fields[k].initial = str(fieldlist[k]['initial'])
