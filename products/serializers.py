from rest_framework import serializers
from products.models import Version


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = (
            'product_id',
            'software',
            'version'
        )


class VersionDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(required=False)
    software = serializers.CharField(required=False)
    version = serializers.CharField(required=False)

    class Meta:
        model = Version
        fields = (
            'product_id',
            'software',
            'version'
        )
