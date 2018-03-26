from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/(?P<day_of_the_week>\w*)$', views.about, name='about'),
]
