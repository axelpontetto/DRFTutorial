from django.urls import path, include
from django.conf.urls import include as include_conf

urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include_conf('rest_framework.urls')),
]
