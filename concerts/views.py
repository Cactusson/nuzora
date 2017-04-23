from django.views import generic

from braces import views

from . import models


class HomePageView(
    views.SuperuserRequiredMixin,
    generic.TemplateView
):
    template_name = 'concerts/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        concerts = models.Concert.objects.all().order_by('-date')
        context['concerts'] = concerts
        return context


class BandListView(
    views.SuperuserRequiredMixin,
    generic.ListView
):
    model = models.Band


class BandDetailView(
    views.SuperuserRequiredMixin,
    generic.DetailView
):
    model = models.Band


class CityListView(
    views.SuperuserRequiredMixin,
    generic.ListView
):
    model = models.City


class CityDetailView(
    views.SuperuserRequiredMixin,
    generic.DetailView
):
    model = models.City


class ConcertDetailView(
    views.SuperuserRequiredMixin,
    generic.DetailView
):
    model = models.Concert


class StatisticsView(
    views.SuperuserRequiredMixin,
    generic.TemplateView
):
    template_name = 'concerts/statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data(**kwargs)
        concerts = models.Concert.objects.all()
        total_concerts = concerts.count()
        total_bands = models.Band.objects.all().count()
        total_cities = models.City.objects.all().count()
        total_money = sum([concert.ticket_price for concert in list(concerts)])
        context['total_concerts'] = total_concerts
        context['total_bands'] = total_bands
        context['total_cities'] = total_cities
        context['total_money'] = total_money
        return context
