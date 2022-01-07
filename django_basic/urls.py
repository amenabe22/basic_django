from django.contrib import admin
from django.urls import path, include

# default: "Django Administration"
admin.site.site_header = 'UKTowns Location Site'
# default: "Site administration"
admin.site.index_title = 'UKTowns Location Site'
admin.site.site_title = 'UKTowns Location Site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('towns.urls'))
]
