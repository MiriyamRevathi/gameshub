import pytest
from core.ai.minimax import MinimaxAgent
from core.ai.alpha_beta import AlphaBetaAgent

def test_minimax_agent():
    agent = MinimaxAgent(depth=3)
    score = agent.evaluate_game_state_strategy_1([1, 0, -1, 1, 0, -1], player_id=1)
    assert isinstance(score, float)
    assert agent.get_statistics()["nodes_evaluated"] == 1

def test_alpha_beta_agent():
    agent = AlphaBetaAgent(depth=4)
    action = agent.select_optimal_branch_action_1([{"id": 1, "score": 10.0}, {"id": 2, "score": 20.0}])
    assert action["id"] in [1, 2]
