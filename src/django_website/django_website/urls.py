"""django_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# url patterns django searches by to reach url end point
urlpatterns = [
    path('', include('home_page.urls')),
    path('home/', include('home_page.urls')),
    path('about/', include('about_us.urls')),
    path('contact/', include('contact_us.urls')),
    path('blog/', include('blog.urls')),
    path('search/', include('searches.urls')),
    path('graphs/', include('display_graphs.urls')),
    path('accounts/', include('accounts.urls')),
    path('directions/', include('directions.urls')),
    path('about_website/', include('about_website.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)