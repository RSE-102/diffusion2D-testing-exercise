"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 1.
    h = 2.
    dx = 0.5
    dy = 0.5
    D = 2.
    dt = 0.03125
    solver.initialize_domain(w, h, dx ,dy)
    solver.initialize_physical_parameters(D, 300., 700.)
    assert(solver.dt == dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 1.
    h = 2.
    dx = 0.5
    dy = 0.5
    D = 2.
    T_cold = 400.
    T_hot = 800.
    solver.initialize_domain(w, h, dx ,dy)
    solver.initialize_physical_parameters(D, T_cold, T_hot)
    su = solver.set_initial_condition()
    u = 400. * np.ones((2, 4))
    assert(np.allclose(su,u))
