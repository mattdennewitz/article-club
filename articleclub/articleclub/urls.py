from django.conf.urls import include, url
from django.contrib import admin

from bundles.api.v1 import urls as bundle_api_v1_urls

urlpatterns = [
    url(r'^api/v1/bundles/', include(bundle_api_v1_urls)),

    url(r'^admin/', include(admin.site.urls)),
]
