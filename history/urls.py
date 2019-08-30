from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from history.filters import PlaceFilter
from history.views import PlaceView, place_list, state_list, place_search

urlpatterns = [
    url(r"^$", state_list),
    # <str:state> is a url variable
    path("search/", place_search),
    path("state/<str:state>/", place_list),
    # <int:pk> is a url variable
    path("place/<int:pk>", PlaceView.as_view())
]

