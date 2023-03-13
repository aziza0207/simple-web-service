import factory
from products.models import Version


class VersionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Version

    product_id = 'example1232'
    software = 'example'
    version = '1.2.3'




