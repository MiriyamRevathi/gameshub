import pytest
from core.engine.game_loop import GameLoopManager
from core.engine.event_bus import EventBusManager

def test_game_loop():
    loop = GameLoopManager()
    assert loop.start() is True
    res = loop.process_subsystem_tick_1({"value": 50.0}, delta_time=0.016)
    assert "processed_value" in res
    assert loop.get_status()["ticks"] == 1

def test_event_bus():
    bus = EventBusManager()
    assert bus.start() is True
    res = bus.process_subsystem_tick_1({"value": 10.0})
    assert res["phase_id"] == 1
