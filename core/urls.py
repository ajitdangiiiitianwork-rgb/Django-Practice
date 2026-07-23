"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import *
from vege.views import *
urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe, name='recipes'),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('delete_recipes/<id>/', delete_recipes, name='delete_recipes'),
    path('update_recipes/<id>/', update_recipes, name='update_recipes'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('students/', get_students, name='get_students')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()