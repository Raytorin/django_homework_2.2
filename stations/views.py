from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    correct_data = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            correct_data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    paginator = Paginator(correct_data, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
