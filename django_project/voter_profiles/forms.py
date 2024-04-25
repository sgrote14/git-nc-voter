from django import forms

from .models import County


class VoterSearchForm(forms.Form):
    county_name = forms.ModelChoiceField(
        label='Select County',
        queryset=County.objects.all().order_by('county_name'),
        empty_label='All Counties',
        required=False)
    search_query = forms.CharField(label='Search by Last Name', required=False)
