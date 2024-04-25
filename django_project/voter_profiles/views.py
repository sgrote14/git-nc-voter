from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from .models import RegisteredVotersActive, County, RegVoterFile, VoterHistory
from .forms import VoterSearchForm


# Create your views here.

def get_county_data():
    party_codes = ['DEM', 'REP', 'UNA']
    county_data = {}
    for party_code in party_codes:
        voter_counts = RegisteredVotersActive.objects.filter(party_code=party_code).values('county_id').annotate(count=Count('county_id')).order_by('-count')
        for county in voter_counts:
            county_name = County.objects.get(pk=county['county_id']).county_name
            if county_name not in county_data:
                county_data[county_name] = {}
            county_data[county_name][party_code] = intcomma(county['count'])
    return county_data

def home(request):
    county_data = get_county_data()

    # voter_counts = RegisteredVotersActive.objects.filter(party_code='DEM').values('county_id').annotate(Count('county_id')).order_by('-county_id__count')
    # county_data = {County.objects.get(pk=county['county_id']).county_name: county['county_id__count'] for county in voter_counts}

    file_date = RegVoterFile.objects.order_by('-file_date').first()
    context = {'county_data': county_data, 'file_date': file_date}
    return render(request, 'index.html', context)


def voter_search(request):
    queryset = RegisteredVotersActive.objects.none()
    search_form = VoterSearchForm(request.GET)

    print(search_form)

    search_field_name = 'last_name'
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            queryset = RegisteredVotersActive.objects.filter(**{f'{search_field_name}__icontains': search_query})
    num_results = len(queryset)
    print(queryset)

    context = {'search_form': search_form, 'queryset': queryset, 'num_results': num_results}

    return render(request, 'search_template.html', context)


def voter_detail(request, ncid):
    voter_info = RegisteredVotersActive.objects.get(pk=ncid)
    voter_history = VoterHistory.objects.filter(reg_voter_id__nc_id=ncid)

    context = {'voter_info': voter_info, 'voter_history': voter_history}

    return render(request, 'voter_detail.html', context)



