import pytest
from core.math.vector import VectorMathEngine
from core.math.matrix import MatrixMathEngine

def test_vector_engine():
    engine = VectorMathEngine(precision=4)
    res = engine.compute_metric_transform_1([1.0, 2.0, 3.0], alpha=1.0, beta=0.5)
    assert len(res) == 3
    assert engine.get_metrics()["operations"] == 1

def test_matrix_engine():
    engine = MatrixMathEngine(precision=4)
    res = engine.compute_metric_transform_1([1.0, 2.0], alpha=1.0, beta=0.5)
    assert len(res) == 2
