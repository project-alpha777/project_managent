from django.urls import path
from . import views  # importujemy nasze widoki

urlpatterns = [
    path('', views.post_list, name='post_list'),  # główny URL
]

