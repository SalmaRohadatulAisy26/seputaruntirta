from django.contrib import admin
from django.urls import path
from univ.views import coba
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('untirta/', coba),
]
