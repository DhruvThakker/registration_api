"""
Registration API URI specification.
Patterns here should simply point to version-specific patterns.
"""
from django.conf.urls import include, url, patterns

urlpatterns = patterns(
    '',

    url(r'^v0/', include('registration_api.v0.urls')),
)
