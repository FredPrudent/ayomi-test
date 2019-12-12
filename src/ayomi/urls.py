from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'', include(views.home), name="ayomi-home"),
]
