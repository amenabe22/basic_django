from django.urls import path
from .views import HomePageView, CountryPage, CountyPage, CountyDetail

urlpatterns = [
    path('', HomePageView.as_view()),
    path('<str:name>/', CountryPage.as_view()),
    path('detail/<str:county>/<str:county_name>/', CountyDetail.as_view()),
    path('<str:country>/<str:county>/', CountyPage.as_view()),
]
