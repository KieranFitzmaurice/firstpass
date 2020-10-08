from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parameter(models.Model):
    value = models.FloatField()
    input_filepath = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='param_user',on_delete=models.PROTECT)
    derivation_documentation = models.FileField(blank=True,upload_to='derivations/')
    data_source = models.ManyToManyField('DataSource',related_name='param_data',blank=True)
    project = models.ManyToManyField('DataSource',related_name='param_project',blank=True)

    def __str__(self):
        return self.input_filepath

class DataSource(models.Model):
    COUNTRY_CHOICES = [('US','United States'),('ZA','South Africa'),('UG','Uganda'),('ZW','Zimbabwe')]

    Author = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    DatePublished = models.DateField(blank=True)
    Country = models.CharField(max_length=255,choices=COUNTRY_CHOICES,blank=True)
    URL = models.URLField(blank=True)
    DOI = models.CharField(max_length=255,blank=True)
    PMID = models.CharField(max_length=255,blank=True)
    ISBN = models.CharField(max_length=255,blank=True)
    arXivID = models.CharField(max_length=255,blank=True)
    hard_copy = models.FileField(blank=True,upload_to='hardcopies/')
    project = models.ManyToManyField('Project',related_name='data_project',blank=True)
    params = models.ManyToManyField('Parameter',related_name='data_param',blank=True)

    def __str__(self):
        return self.Author+' et al. - '+self.Title

class Project(models.Model):
    name = models.CharField(max_length=30,unique=True)
    abstract = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='project_user',on_delete=models.PROTECT)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.PROTECT)
    params = models.ManyToManyField('Parameter',related_name='project_param',blank=True)
    data_source = models.ManyToManyField('DataSource',related_name='project_data',blank=True)

    def __str__(self):
        return self.name
