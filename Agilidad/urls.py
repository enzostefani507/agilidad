from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/',include('perfil.urls')),
    path('estado/',include('estado.urls')),
    path('felicidad/',include('felicidad.urls')),
    path('',include('home.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
