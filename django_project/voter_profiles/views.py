import json

from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RegisteredVotersActive, County, RegVoterFile, VoterHistory
from .forms import VoterSearchForm


# Create your views here.

def get_county_data():
    party_codes = ['DEM', 'REP', 'UNA']
    county_data = {}
    for party_code in party_codes:
        voter_counts = RegisteredVotersActive.objects.filter(party_code=party_code).values('county_id').annotate(
            count=Count('county_id')).order_by('-count')
        for county in voter_counts:
            county_id = county['county_id']
            county_name = County.objects.get(pk=county['county_id']).county_name
            if county_id not in county_data:
                county_data[county_id] = {'county_name': county_name}
            county_data[county_id][party_code] = intcomma(county['count'])
    print("county data:", county_data)
    return county_data


def home(request):
    county_data = get_county_data()

    file_date = RegVoterFile.objects.order_by('-file_date').first()
    context = {'county_data': county_data, 'file_date': file_date}
    return render(request, 'index.html', context)


def county_view(request, county_id):
    county_info = County.objects.get(pk=county_id)
    context = {'county_info': county_info}
    return render(request, 'county_detail.html', context)


def search_filter(form):
    print(form.cleaned_data)
    filters = {}

    county_id = form.cleaned_data['county_id']
    precinct_name = form.cleaned_data['precinct_desc']
    party_name = form.cleaned_data['party_code']
    search_query = form.cleaned_data['last_name']

    fields = list(form.cleaned_data.keys())
    print(fields)

    for key, value in form.cleaned_data.items():
        if value:
            if type(value) == str:
                filters[f'{key}__icontains'] = value
            else:
                filters[f'{key}'] = value

    filter_conditions = Q()
    for key, value in filters.items():
        filter_conditions &= Q(**{key: value})

    print('filter_conditions:', filter_conditions)
    return filter_conditions


def voter_search(request):
    queryset = RegisteredVotersActive.objects.none()
    search_form = VoterSearchForm(request.GET)
    print('request.GET:', request.GET)

    if request.GET:
        if request.GET['county_id']:
            county_id = request.GET['county_id']
            precinct_choices = get_precincts_choice(request)
            search_form.fields['precinct_desc'].choices = precinct_choices

    if search_form.is_valid():
        print('search_form:', search_form.cleaned_data)
        filter_conditions = search_filter(search_form)
        queryset = RegisteredVotersActive.objects.filter(filter_conditions, status_code='A')
    else:
        print("Form data:", request.GET)
        print("Form errors:", search_form.errors)

    num_results = len(queryset)
    context = {'search_form': search_form, 'queryset': queryset, 'num_results': num_results}

    return render(request, 'search_template.html', context)


def get_precincts(request):
    county_id = request.GET.get('county_id')
    print(county_id)
    precincts = RegisteredVotersActive.objects.filter(county_id=county_id).values_list('precinct_desc',
                                                                                       flat=True).distinct().order_by(
        'precinct_desc')
    return JsonResponse(list(precincts), safe=False)


def get_precincts_choice(request):
    county_id = request.GET.get('county_id')
    precincts = RegisteredVotersActive.objects.filter(county_id=county_id).values_list('precinct_desc', flat=True).distinct().order_by('precinct_desc')
    precinct_choices = [(precinct, precinct) for precinct in precincts]
    return precinct_choices


def voter_detail(request, ncid):
    voter_info = RegisteredVotersActive.objects.get(pk=ncid)
    voter_history = VoterHistory.objects.filter(reg_voter_id__nc_id=ncid).order_by('-election_date')
    context = {'voter_info': voter_info, 'voter_history': voter_history}
    for voter in voter_history:
        print(voter.election_date)

    return render(request, 'voter_detail.html', context)
