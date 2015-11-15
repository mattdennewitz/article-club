from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^(?P<bundle_id>\d+)/add/$', views.add_link_to_bundle,
        name='add-link-to-bundle'),
    url(r'^new/$', views.CreateBundleView.as_view(),
        name='create-bundle'),
    url(r'^search/$', views.find_bundles_for_url,
        name='find-bundles-for-url'),
]
