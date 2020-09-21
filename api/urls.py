from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
