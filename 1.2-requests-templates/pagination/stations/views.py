from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


BUS_STATION_CSV = settings.BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)

    page_number = int(request.GET.get('page', 1))

    paginator = Paginator(data, 10)
    stations = paginator.get_page(page_number)

    context = {
        'bus_stations': stations,
        'page': stations
    }

    return render(request, 'stations/index.html', context)
