from django.urls import include, path

urlpatterns = [
    path("placeholders/", include("django_placeholdit.urls", namespace="placeholdit")),
]
