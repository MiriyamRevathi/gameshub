import pytest
from api.routes import APIRouter
from api.auth_api import AuthAPI

def test_api_routes():
    router = APIRouter()
    res = router.handle_endpoint_v1_1({"query": "test"})
    assert res["code"] == 200

def test_auth_api():
    auth_api = AuthAPI()
    res = auth_api.handle_endpoint_v1_1({"user": "admin"})
    assert res["code"] == 200
