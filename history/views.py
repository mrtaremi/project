import json
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from history.filters import PlaceFilter
from history.models import State, Place, Category


from django.core.paginator import Paginator


def state_list(request):
    f = PlaceFilter(request.GET, queryset=Place.objects.all())
    s = State.objects.all()
    randomed = random.choice(Place.objects.all())
    return render(request, 'history/state_list.html', {'filter': f, 'state_list': s, 'randomed': randomed})


def place_search(request):
    f = PlaceFilter(request.GET, queryset=Place.objects.filter())
    randomed = random.choice(Place.objects.all())
    return render(request, 'history/place_filter.html', {'filter': f, "randomed": randomed})


def place_list(request, state):
    



    print(Place.objects.all()[0].image.all())
    f = PlaceFilter(request.GET, queryset=Place.objects.filter(state__en_name=state))
    category = Category.objects.all()
    randomed = random.choice(Place.objects.all())
    
    return render(request, 'history/place_filter.html', {'filter': f, 'category': category, 'randomed': randomed})


class PlaceView(DetailView):
    model = Place

    def get_context_data(self, **kwargs):
        context = super(PlaceView, self).get_context_data(**kwargs)
        randomed = random.choice(Place.objects.all())
        context.update({'randomed': randomed})
        return context


def add(request):
    with open("./Province.json", "r", encoding="utf8") as f:
        json_data = json.load(f)
        for state in json_data:
            State.objects.create(name=state['name'], en_name=state['en_name'])
        f.close()
        return HttpResponse("Ok")




def addp(request):
    with open("./FakePlace.json", "r", encoding="utf8") as f:
        json_data = json.load(f)
        for state in json_data:
            Place.objects.create(id=state['id'], name=state['name'], thumb=state['thumb'], desc=state['desc'], url=state['url'], category_id=state['category_id'], state_id=state['state_id'])
        f.close()
        return HttpResponse("Ok")
