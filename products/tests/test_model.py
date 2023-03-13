import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from products.models import Version
from products.serializers import VersionSerializer, VersionDetailSerializer

client = APIClient()


@pytest.mark.django_db
class TestModel:

    def test_create_version(self):
        url = reverse("versions")
        payload = {"product_id": "aaaa1232",
                   "software": "samba",
                   "version": "1.2.3"
                   }
        response = client.post(url, data=payload)
        assert response.status_code == status.HTTP_201_CREATED

    def test_list_versions(self):
        url = reverse("versions")
        response = client.get(url)
        posts = Version.objects.all()
        expected_data = VersionSerializer(posts, many=True).data
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data

    def test_get_version(self, version):
        url = reverse("version-details", kwargs={"pk": version.id})
        response = client.get(url)
        expected_data = VersionDetailSerializer(version).data
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data

    def test_update_version(self, version):
        url = reverse("version-details", kwargs={"pk": version.id})
        payload = {"product_id": "example1234",
                   "software": "example123",
                   "version": "1.2.3.4",
                   }
        response = client.put(url, data=payload)
        assert response.status_code == status.HTTP_200_OK

    def test_delete_version(self, version):
        url = reverse("version-details", kwargs={"pk": version.id})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
