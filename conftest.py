import pytest
from pytest_factoryboy import register
from products.tests.factories import VersionFactory

register(VersionFactory)


@pytest.fixture
def version(db, version_factory):
    version = version_factory.create()
    return version
