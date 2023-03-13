from django.urls import path
from products.views import (
    ListCreateVersion, VersionDetail,


)

urlpatterns = [path('versions/', ListCreateVersion.as_view(), name="versions"),
               path('version/<int:pk>', VersionDetail.as_view(), name="version-details")]

