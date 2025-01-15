import pytest
from rest_framework.test import APIClient

from logistic.models import Product, Stock


@pytest.fixture
def client():
	return APIClient()

@pytest.mark.django_db
def test_get_index(client):
	response = client.get("/api/v1/")
	assert response.status_code == 200