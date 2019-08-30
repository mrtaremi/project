from django import forms
from django.contrib.auth.models import User, Group
import django_filters

from history.models import Category, Place


class PlaceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    state__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Place
        fields = ['name', "state__name"]
