from django.contrib.auth.models import User
from .models import Parameter, DataSource
import django_filters

class ParameterFilter(django_filters.FilterSet):

    class Meta:
        model = Parameter
        fields = ['type', 'created_at', 'created_by', 'status']

class DataSourceFilter(django_filters.FilterSet):
    Title = django_filters.CharFilter(label="Title contains",lookup_expr='icontains')
    Author = django_filters.CharFilter(label="Author or publisher",lookup_expr='icontains')
    Date_published = django_filters.DateFilter(label="Published after",lookup_expr='gt')
    created_by = django_filters.ModelChoiceFilter(label="Uploaded by",queryset=User.objects.all())
    class Meta:
        model = DataSource
        fields = ['Title','Author','PubType','Date_published','Country','created_by']
