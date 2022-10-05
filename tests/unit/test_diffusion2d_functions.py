"""
Tests for functions in class SolveDiffusion2D
"""
import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D
from unittest import TestCase

class TestDiffusion2D(TestCase):
    def setUp(self):
        # plate size, mm
        self.w = 20.
        self.h = 20.

        # intervals in x-, y- directions, mm
        self.dx = 1.
        self.dy = 1.

        # Thermal diffusivity of steel, mm^2/s
        self.D = 5.

        # Initial cold temperature of square domain
        self.T_cold = 200.

        # Initial hot temperature of circular disc at the center
        self.T_hot = 500.

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(self.w, self.h, self.dx, self.dy)
        self.assertEqual(solver.nx, 20)
        self.assertEqual(solver.ny, 20)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 1.
        solver.dy = 1.
        solver.initialize_physical_parameters(self.D, self.T_cold, self.T_hot)
        expected_dt = 0.05
        self.assertAlmostEqual(solver.dt, expected_dt, 2)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.dx = 10.
        solver.dy = 10.
        solver.T_cold = 200.
        solver.T_hot = 500.
        solver.nx = 3
        solver.ny = 3
        u0 = solver.set_initial_condition()
        expected_u0 = np.array([[200., 200., 200.],[200., 200., 200.],[200., 200., 200.]])
        self.assertAlmostEqual(u0[0,0], expected_u0[0,0], 3)
