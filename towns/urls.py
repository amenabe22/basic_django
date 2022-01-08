from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('add/', views.populate_towns_data, name='add'),
    path('<str:country>/', views.CountryPage.as_view()),
    path('detail/<str:county>/<str:county_name>/', views.CountyDetail.as_view()),
    path('<str:country>/<str:county>/', views.CountyPage.as_view()),
]
