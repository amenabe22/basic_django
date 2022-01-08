from .models import UkTowns
from django.db.models import Count
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # get the current context
        context = super().get_context_data(**kwargs)
        all_countries = UkTowns.objects.values(
            'country').annotate(Count('id')).distinct()
        context['countries'] = all_countries
        return context


class CountryPage(TemplateView):
    template_name = "country.html"

    def get_context_data(self, country, **kwargs):
        # get the country
        country = UkTowns.objects.filter(country=country).values(
            'county', 'country').annotate(Count('id')).distinct()
        if not country.first():
            raise Http404
        ctx = super().get_context_data(**kwargs)
        ctx["country"] = country.first()
        ctx["counties"] = country
        return ctx


class CountyPage(TemplateView):
    template_name = "county.html"

    def get_context_data(self, country, county, **kwargs):
        # get the country
        country = UkTowns.objects.filter(country=country, county=county)
        county_set = UkTowns.objects.filter(county=county)
        print(country.first(), "bpt1")
        if not country.first():
            raise Http404
        ctx = super().get_context_data(**kwargs)
        ctx["country"] = country.first()
        ctx["counties"] = country
        ctx["names"] = county_set
        return ctx


class CountyDetail(TemplateView):
    template_name = "county_detail.html"

    def get_context_data(self, county, county_name, **kwargs):
        county_obj = UkTowns.objects.filter(name=county_name).first()
        if not county_obj:
            raise Http404
        # county = UkTowns.objects.filter(name=county_name).first()
        # print(county,"county caught")
        if not county:
            raise Http404
        ctx = super().get_context_data(**kwargs)
        ctx["cnt_obj"] = county_obj
        return ctx


@csrf_exempt
def populate_towns_data(request):
    if request.POST:
        payload = request.POST
        print(request.POST, "payload")
        UkTowns.objects.create(
            name=payload["name"].replace("/", ""),
            county=payload["county"].replace("/", ""),
            country=payload["country"].replace("/", ""),
            grid_reference=payload["grid_reference"],
            easting=payload["easting"],
            northing=payload["northing"],
            latitude=payload["latitude"],
            longitude=payload["longitude"],
            postcode_sector=payload["postcode_sector"],
            nuts_region=payload["nuts_region"],
            type=payload["type"],
        )
        return JsonResponse({"test": "message"})
    data = {"message": "Hey there"}
    return JsonResponse(data)
