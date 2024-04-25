from django import forms


class VoterSearchForm(forms.Form):
    search_query = forms.CharField(label='Search by Last Name', required=True)