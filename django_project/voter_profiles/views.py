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


def voter_search(request):
    queryset = RegisteredVotersActive.objects.none()
    search_form = VoterSearchForm(request.GET)
    print("Form instance:", search_form)

    search_field_name = 'last_name'
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        county_name = search_form.cleaned_data.get('county_name')
        print(search_query, county_name)
        if search_query and county_name:
            queryset = RegisteredVotersActive.objects.filter(**{f'{search_field_name}__icontains': search_query})
            queryset = queryset.filter(county_id=county_name.county_id)

        elif county_name:
            queryset = RegisteredVotersActive.objects.filter(county_id=county_name.county_id)

        elif search_query:
            queryset = RegisteredVotersActive.objects.filter(**{f'{search_field_name}__icontains': search_query})

        else:
            queryset = RegisteredVotersActive.objects.none()



    else:
        print("Form data:", request.GET)
        print("Form errors:", search_form.errors)

    print(len(queryset))
    queryset = queryset.filter(status_code='A')
    print(len(queryset))
    num_results = len(queryset)

    context = {'search_form': search_form, 'queryset': queryset, 'num_results': num_results}

    return render(request, 'search_template.html', context)


def voter_detail(request, ncid):
    voter_info = RegisteredVotersActive.objects.get(pk=ncid)
    voter_history = VoterHistory.objects.filter(reg_voter_id__nc_id=ncid).order_by('-election_date')
    context = {'voter_info': voter_info, 'voter_history': voter_history}
    for voter in voter_history:
        print(voter.election_date)

    return render(request, 'voter_detail.html', context)
