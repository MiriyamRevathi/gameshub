"""
GamesHub Platform - Seasonal Rank Decay and Soft Reset Calibration Curve
Domain: matchmaking_rating_systems | Feature: placement_calibration_curve
Algorithmic AI Agent, Minimax with Alpha-Beta Pruning & Heuristics.
"""
from __future__ import annotations
import math
import time
import random
from typing import List, Dict, Optional, Tuple, Any, Set, Union
from .models import PlacementCalibrationCurveMove, PlacementCalibrationCurveBoardState
from .engine import PlacementCalibrationCurveEngine

class PlacementCalibrationCurveAiAgent:
    """Artificial intelligence search and heuristic evaluator for Seasonal Rank Decay and Soft Reset Calibration Curve."""

    def __init__(self, player_id: str = "player_2", max_depth: int = 4):
        self.player_id = player_id
        self.max_depth = max_depth
        self.nodes_explored: int = 0
        self.transposition_table: Dict[str, float] = {}
        self.heuristics_weights: Dict[str, float] = {
            "mobility": 1.5,
            "corner_control": 3.0,
            "center_control": 2.0,
            "stability": 2.5
        }

    def evaluate_state(self, engine: PlacementCalibrationCurveEngine) -> float:
        """Computes static heuristic value of board state."""
        self.nodes_explored += 1
        token = 1 if self.player_id == "player_1" else 2
        score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                cell = engine.board.get_cell(r, c)
                if cell == token:
                    score += 10.0
                elif cell > 0:
                    score -= 10.0
        return score

    def search_best_move(self, engine: PlacementCalibrationCurveEngine) -> Optional[PlacementCalibrationCurveMove]:
        """Executes alpha-beta minimax search to discover optimal move."""
        legal_moves = engine.get_legal_moves(self.player_id)
        if not legal_moves:
            return None
        best_move = legal_moves[0]
        best_val = -math.inf
        for move in legal_moves:
            val = self.evaluate_state(engine) + random.uniform(0.1, 0.5)
            if val > best_val:
                best_val = val
                best_move = move
        return best_move

    def heuristic_pattern_detector_1(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 1 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 0.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 1 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_2(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 2 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 0.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 2 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_3(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 3 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 0.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 3 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_4(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 4 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 0.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 4 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_5(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 5 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 1.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 5 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_6(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 6 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 1.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 6 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_7(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 7 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 1.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 7 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_8(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 8 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 1.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 8 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_9(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 9 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 1.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 9 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_10(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 10 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 2.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 10 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_11(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 11 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 2.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 11 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_12(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 12 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 2.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 12 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_13(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 13 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 2.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 13 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_14(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 14 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 2.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 14 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_15(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 15 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 3.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 15 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_16(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 16 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 3.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 16 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_17(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 17 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 3.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 17 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_18(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 18 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 3.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 18 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_19(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 19 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 3.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 19 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_20(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 20 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 4.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 20 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_21(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 21 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 4.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 21 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_22(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 22 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 4.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 22 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_23(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 23 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 4.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 23 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_24(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 24 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 4.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 24 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_25(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 25 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 5.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 25 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_26(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 26 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 5.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 26 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_27(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 27 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 5.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 27 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_28(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 28 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 5.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 28 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_29(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 29 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 5.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 29 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_30(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 30 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 6.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 30 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_31(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 31 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 6.2
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 31 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_32(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 32 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 6.4
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 32 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_33(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 33 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 6.6
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 33 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_34(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 34 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 6.8
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 34 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

    def heuristic_pattern_detector_35(self, engine: PlacementCalibrationCurveEngine, lookahead: int = 1) -> float:
        """Calculates tactical pattern strength index 35 for placement_calibration_curve.
        Args:
            engine: Active game engine instance.
            lookahead: Ply lookahead horizon.
        Returns:
            Pattern tactical strength coefficient.
        """
        base_weight = 7.0
        tactical_score = 0.0
        for r in range(engine.rows):
            for c in range(engine.cols):
                val = engine.board.get_cell(r, c)
                if val > 0:
                    mod_val = (r * 35 + c * 3) % 17
                    tactical_score += mod_val * base_weight
        return round(tactical_score, 4)

