from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parameter(models.Model):
    value = models.FloatField()
    input_filepath = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='param_creator',on_delete=models.PROTECT)
    modified_at = models.DateTimeField(auto_now_add=True,blank=True)
    modified_by = models.ForeignKey(User,related_name='param_modifier',on_delete=models.PROTECT)
    derivation_documentation = models.FileField(upload_to='derivations/',blank=True)
    data_sources = models.ManyToManyField('DataSource',related_name='param_data',blank=True)
    projects = models.ManyToManyField('Project',related_name='param_project',blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.input_filepath

class DataSource(models.Model):
    COUNTRY_CHOICES = [('United States','United States'),('South Africa','South Africa'),('Uganda','Uganda'),('Zimbabwe','Zimbabwe')]
    PUBTYPE_CHOICES = [('Journal article','Journal article'),('Pre-print','Pre-print'),('Website','Website'),('Government report','Government report'),('NGO report','NGO report'),('Other','Other')]
    PubType = models.CharField(max_length=255,verbose_name="Publication type",choices=PUBTYPE_CHOICES)
    Author = models.CharField(max_length=255,help_text="surname of lead author (if article)",verbose_name="Author or publisher")
    Title = models.CharField(max_length=255,verbose_name="Title")
    Date_published = models.DateField(blank=True,verbose_name="Date published",help_text="yyyy-mm-dd")
    Country = models.CharField(max_length=255,verbose_name="Country / Setting",choices=COUNTRY_CHOICES,blank=True)
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
