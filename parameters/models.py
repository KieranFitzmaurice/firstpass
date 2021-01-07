from django.db import models
from django.contrib.auth.models import User
from parameters.choices import country_options, publication_options, parameter_options, status_options, get_default_json
import parameters.json_helper_functions as jf

# Create your models here.

class Parameter(models.Model):
    PARAMTYPE_CHOICES = parameter_options()
    STATUS_CHOICES = status_options()
    value = models.CharField(max_length=255)
    type = models.CharField(max_length=255,verbose_name="Type",choices=PARAMTYPE_CHOICES)
    input_filepath = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='param_creator',on_delete=models.PROTECT)
    modified_at = models.DateTimeField(auto_now_add=True,blank=True)
    modified_by = models.ForeignKey(User,related_name='param_modifier',on_delete=models.PROTECT)
    derivation_documentation = models.FileField(upload_to='derivations/',blank=True)
    data_sources = models.ManyToManyField('DataSource',related_name='param_data',blank=True)
    projects = models.ManyToManyField('Project',related_name='param_project',blank=True)
    status = models.CharField(max_length=225,verbose_name="Status",choices=STATUS_CHOICES,default="Currently in use")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.input_filepath

class DataSource(models.Model):
    COUNTRY_CHOICES = country_options()
    PUBTYPE_CHOICES = publication_options()
    PubType = models.CharField(max_length=255,verbose_name="Publication type",choices=PUBTYPE_CHOICES)
    Author = models.CharField(max_length=255,help_text="surname of lead author (if article)",verbose_name="Author or publisher")
    Title = models.CharField(max_length=255,verbose_name="Title")
    Date_published = models.DateField(verbose_name="Date published",help_text="yyyy-mm-dd")
    Country = models.CharField(max_length=255,verbose_name="Country / Setting",choices=COUNTRY_CHOICES,default="None")
    CountryCode = models.CharField(max_length=10)
    URL = models.URLField(blank=True,verbose_name="URL")
    DOI = models.CharField(max_length=255,blank=True)
    PMID = models.CharField(max_length=255,blank=True)
    hard_copy = models.FileField(blank=True,verbose_name="Saved copy of file",upload_to='hardcopies/')
    projects = models.ManyToManyField('Project',related_name='data_project',blank=True)
    parameters = models.ManyToManyField('Parameter',related_name='data_param',blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='datasource_creator',on_delete=models.PROTECT)
    modified_at = models.DateTimeField(auto_now_add=True,blank=True)
    modified_by = models.ForeignKey(User,related_name='datasource_modifier',on_delete=models.PROTECT)

    def __str__(self):
        if self.PubType in ["Journal article","Pre-print"]:
            return self.Author+' et al. - '+self.Title
        else:
            return self.Author+' - '+self.Title

class InFile(models.Model):
    DEFAULT_JSON = get_default_json()
    DEFAULT_LEDGER = jf.build_metadata_ledger(DEFAULT_JSON)
    DEFAULT_FIELDLIST = jf.build_field_ledger(DEFAULT_JSON)
    info = models.JSONField(default = DEFAULT_JSON)
    ledger = models.JSONField(default = DEFAULT_LEDGER)
    fieldlist = models.JSONField(default = DEFAULT_FIELDLIST)

class Project(models.Model):
    name = models.CharField(max_length=30,unique=True)
    abstract = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='project_user',on_delete=models.PROTECT)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.PROTECT)
    parameters = models.ManyToManyField('Parameter',related_name='project_param',blank=True)
    data_sources = models.ManyToManyField('DataSource',related_name='project_data',blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
