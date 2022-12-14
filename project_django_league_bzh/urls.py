from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('league_bzh/', include('league_bzh.urls')),
    path('admin/', admin.site.urls),
]
