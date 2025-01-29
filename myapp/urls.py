from django.contrib import admin
from django.urls import path, include  # include is necessary to add app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userform.urls')),  # Include userform's URLs
]
