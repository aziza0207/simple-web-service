import pytest
from pytest_factoryboy import register
from products.tests.factories import VersionFactory

register(VersionFactory)


