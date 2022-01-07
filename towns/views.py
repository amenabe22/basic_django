from re import template
from django.shortcuts import render
from .models import Country, County, UkTowns, CountyName
from django.http import Http404
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # get the current context
        context = super().get_context_data(**kwargs)
        all_countries = Country.objects.all()
        context['countries'] = all_countries
        return context


class CountryPage(TemplateView):
    template_name = "country.html"

    def get_context_data(self, name, **kwargs):
        # get the country
        country = Country.objects.filter(name=name).first()
        if not country:
            raise Http404
        all_counties = County.objects.filter(country=country)
        ctx = super().get_context_data(**kwargs)
        ctx["country"] = country
        ctx["counties"] = all_counties
        return ctx


class CountyPage(TemplateView):
    template_name = "county.html"

    def get_context_data(self, country, county, **kwargs):
        # get the country
        country = Country.objects.filter(name=country).first()
        if not country:
            raise Http404
        county = County.objects.filter(name=county).first()
        if not county:
            raise Http404
        ctx = super().get_context_data(**kwargs)
        ctx["names"] = county.county_name.all()
        ctx["country"] = country
        ctx["county"] = county
        return ctx


class CountyDetail(TemplateView):
    template_name = "county_detail.html"

    def get_context_data(self, county, county_name, **kwargs):
        county_name = CountyName.objects.filter(name=county_name).first()
        if not county_name:
            raise Http404
        county = County.objects.filter(name=county).first()
        if not county:
            raise Http404
        ctx = super().get_context_data(**kwargs)
        ctx["name"] = county_name
        ctx["county"] = county
        return ctx
