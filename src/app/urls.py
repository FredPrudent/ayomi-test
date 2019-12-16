from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from ayomi.views import account_redirect


urlpatterns = [
        # Examples:
    url(r'^$', 'ayomi.views.home', name='home'),
    url(r'^profile/', 'ayomi.views.profile', name='profile'),
    url(r'^login/', 'ayomi.views.login', name='login'),
    url(r'^logout/', 'ayomi.views.logout', name='logout'),
    url(r'^account/$', account_redirect, name='account-redirect'),

    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
