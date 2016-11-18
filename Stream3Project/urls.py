"""Stream3Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from homeApp import views as homeApp_views
from accountsApp import views as accountsApp_views
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeApp_views.get_index, name='index'),
    url(r'^register/$', accountsApp_views.register, name='register'),
    url(r'^profile/$', accountsApp_views.profile, name='profile'),
    url(r'^login/$', accountsApp_views.login, name='login'),
    url(r'^logout/$', accountsApp_views.logout, name='logout'),
    url(r'', include('blogApp.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^cancel_subscription/$', accountsApp_views.cancel_subscription, name='cancel_subscription'),
    url(r'^cancellation/$', accountsApp_views.cancellation, name='cancellation'),



]
