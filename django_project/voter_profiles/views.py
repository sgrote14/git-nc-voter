from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from .models import RegisteredVotersActive, County, RegVoterFile


# Create your views here.
def home(request):
    voter_counts = RegisteredVotersActive.objects.filter(party_code='DEM').values('county_id').annotate(Count('county_id')).order_by('-county_id__count')
    county_data = {County.objects.get(pk=county['county_id']).county_name: county['county_id__count'] for county in voter_counts}
    file_date = RegVoterFile.objects.order_by('-file_date').first()
    context = {'county_data': county_data, 'file_date': file_date}
    return render(request, 'index.html', context)


def voter_search(request):
    return HttpResponse("Placeholder")
