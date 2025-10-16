"""
URL configuration for cim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.urls import core_urlpatterns
from organization.urls import organization_urlspatterns
from requests.urls import requests_urlspatterns
from surveys.urls import surveys_urlspatterns
from users.urls import users_urlspatterns

urlpatterns = [
    path('',include(core_urlpatterns)),
    path('admin/', admin.site.urls),
    path('organization/',include(organization_urlspatterns)),
    path('requests/',include(requests_urlspatterns)),
    path('surveys/',include(surveys_urlspatterns)),
    path('users/',include(users_urlspatterns)),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('registration.urls')),

]
