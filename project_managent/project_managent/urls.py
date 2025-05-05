from django.contrib import admin
from django.urls import path, include  # include jest ważne!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cv.urls')),  # kierujemy ruch na aplikację cv
]
