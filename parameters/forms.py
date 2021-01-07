from django import forms
from parameters.models import Parameter, DataSource, Project
from parameters.choices import country_options, publication_options, parameter_options, parameter_pretty_options, status_options
from parameters.validators import validate_integer_list
from django.core.validators import MinLengthValidator
import parameters.json_helper_functions as jf

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

    def __init__(self, *args, **kwargs):
        # Construct an arbitrary form based on the infile model's fieldlist field
        # Make sure to pop fieldlist out of kwargs before super().__init__() since it's unsupported by the parent class forms.Form
        fieldlist = kwargs.pop('fieldlist')
        super(EditJSONForm, self).__init__(*args, **kwargs)
        klist = list(fieldlist.keys())
        for k in klist:
            if fieldlist[k]['data_type'] == 'number':
                # Paradoxically, you need to make required=False in order to later on check if the field is blank
                self.fields[k] = forms.FloatField(required=False,widget=forms.NumberInput(attrs={'class':'custom-number-input'}))
                self.fields[k].initial = fieldlist[k]['initial']

            elif fieldlist[k]['data_type'] == 'string':
                self.fields[k] = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom-string-input'}))
                self.fields[k].initial = fieldlist[k]['initial']

            elif fieldlist[k]['data_type'] == 'boolean':
                self.fields[k] = forms.ChoiceField(required=True,widget=forms.RadioSelect(attrs={'class': 'custom-boolean-input'}),
                choices=[(True, 'True'),(False, 'False')])
                self.fields[k].initial = fieldlist[k]['initial']

            elif fieldlist[k]['data_type'] == 'list':
                self.fields[k] = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom-string-input'}))
                self.fields[k].initial = str(fieldlist[k]['initial'])
                self.fields[k].validators.append(validate_integer_list) # Add a custom validator to check user input for lists

            else: # null value - haven't figured out if I need this or not. May not work yet.
                self.fields[k] = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'custom-string-input'}))
                self.fields[k].initial = str(fieldlist[k]['initial'])

    def clean(self):
        super(EditJSONForm,self).clean()

        # Check for blank fields. I'm doing it this way instead of just making the fields required because I want to point the user to where the blank fields are.
        klist= self.cleaned_data.keys()
        for k in klist:
            if not self.cleaned_data.get(k) and self.cleaned_data.get(k) != 0:
                    print('hey')
                    self._errors[k] = self.error_class(['Field was left blank. Please enter a value.'])
        return self.cleaned_data


    def process(self, fieldlist):
        # Assumes .cleaned_data exists (need to have already invoked form.is_valid() before form.process())
        # Inserts values into nested dictionary x
        formdata = self.cleaned_data

        # Formdata is a dictionary whose keys are identical to fieldlist (we set it up this way when initializing form)
        klist = list(fieldlist.keys())

        for k in klist:
            if fieldlist[k]['data_type'] == 'list':
                # Need to coerce data from string to list (we've already ensured this is possible in validation)
                formdata[k] = jf.string_to_integer_list(formdata[k])

        return formdata
