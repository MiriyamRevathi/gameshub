import pytest
from services.auth_service import AuthService
from services.game_service import GameService

def test_auth_service():
    auth = AuthService()
    res = auth.handle_service_operation_1("user_123", {"action": "login"})
    assert res["status"] == "success"
    assert "tx_user_123_1_1" in res["transaction_id"]

def test_game_service():
    game = GameService()
    res = game.handle_service_operation_1("user_123", {"game": "chess"})
    assert res["status"] == "success"
