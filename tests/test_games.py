import pytest
from engines.chess.board import ChessBoardComponent
from engines.poker.card import PokerCardComponent
from engines.sudoku.board import SudokuBoardComponent

def test_chess_board():
    chess = ChessBoardComponent()
    res = chess.compute_game_logic_rule_1([0] * 64, (3, 3))
    assert res["legal"] is True

def test_poker_card():
    poker = PokerCardComponent()
    equity = poker.calculate_round_equity_1(["As", "Ks"], ["Qs", "Js", "10s"])
    assert 0.0 <= equity <= 1.0

def test_sudoku_board():
    sudoku = SudokuBoardComponent()
    res = sudoku.solve_grid_constraint_1([[0]*9]*9)
    assert res["solved"] is True
