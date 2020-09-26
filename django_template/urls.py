"""django_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django_template.views import FrontendAppView

urlpatterns = [
    path('posts/', include('api.urls')),
    path('admin/', admin.site.urls),
]

# Makes media accessible in development
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Keep FrontendAppView on the bottom for BrowserHistory urls to work.

# Add any backend paths to the regex, separated by pipes, in order to let Django
# add a trailing slash to them.
# For example, to add a new path 'login' to the site, add it to urlpatterns
# and change `(admin|posts)` to `(admin|posts|login)`

urlpatterns.append(re_path(r'^(?!(admin|posts))', FrontendAppView.as_view()))
