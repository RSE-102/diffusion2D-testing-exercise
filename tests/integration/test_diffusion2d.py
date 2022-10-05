"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(20., 20., 1., 1.)
    solver.initialize_physical_parameters(5., 200., 500.)
    expected_dt = pytest.approx(0.05, rel=1e-2)
    assert solver.dt == expected_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_condition
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(30., 30., 10., 10.)
    solver.initialize_physical_parameters(5., 200., 500.)
    u0 = solver.set_initial_condition()
    expected_u0 = pytest.approx(np.array([[200., 200., 200.],[200., 200., 200.],[200., 200., 200.]]), rel=1e-2)
    assert u0 == expected_u0
