from django import forms
from django.db.models import Q

from .models import County, PartyCode, VoterHistory


def label_from_instance(obj):
    return obj.county_name


class VoterSearchForm(forms.Form):
    county_id = forms.ModelChoiceField(
        label='',
        empty_label='Select a County',
        queryset=County.objects.all().order_by('county_name'),
        required=False,
        widget=forms.Select(attrs={'class': 'search-form-field'})
    )
    precinct_desc = forms.ChoiceField(
        label='',
        required=False,
        choices=[],
        widget=forms.Select(attrs={'class': 'search-form-field',
                                   'placeholder': 'Select Precinct'})
    )

    party_code = forms.ModelChoiceField(
        label='',
        empty_label='All Parties',
        queryset=PartyCode.objects.all().order_by('party_desc'),
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Party', 'class': 'search-form-field'})
    )

    # election_votes = forms.ModelChoiceField(
    #     label='',
    #     empty_label='All Elections',
    #     required=False,
    #     queryset=VoterHistory.objects.filter(Q(election_description__regex=r"\d{2}/\d{2}/\d{4}\s+(GENERAL|PRIMARY)$")).
    #     values_list('election_description', flat=True).distinct(),
    #     widget=forms.Select(attrs={'class': 'search-form-field'})
    # )

    last_name = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by Last Name', 'class': 'search-form-field'})
    )

    def __init__(self, *args, **kwargs):
        super(VoterSearchForm, self).__init__(*args, **kwargs)
        self.fields['county_id'].label_from_instance = label_from_instance

    def clean(self):
        cleaned_data = super().clean()
        county_id = cleaned_data.get('county_id')
        precinct_desc = cleaned_data.get('precinct_desc')
        party_code = cleaned_data.get('party_code')
        last_name = cleaned_data.get('last_name')
        election_votes = cleaned_data.get('election_votes')

        # Check if at least one field is provided
        if not (county_id or precinct_desc or party_code or last_name or election_votes):
            raise forms.ValidationError("At least one field is required.")

        return cleaned_data
