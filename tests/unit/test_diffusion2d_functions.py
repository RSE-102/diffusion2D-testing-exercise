"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase

class TestDiffusion2D(TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 1.
        h = 2.
        dx = 0.5
        dy = 0.5
        nx = 2.
        ny = 4.
        self.solver.initialize_domain(w, h, dx, dy)
        self.assertAlmostEqual(self.solver.nx, nx, 0.1)
        self.assertAlmostEqual(self.solver.ny, ny, 0.1)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        D = 2.
        dt = 0.03125

        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.solver.initialize_physical_parameters(D, 300., 700.)
        self.assertAlmostEqual(self.solver.dt, dt, 0.1)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        T_cold = 400.
        T_hot = 800.
        u = T_cold

        self.solver.T_cold = 400.
        self.solver.T_hot = 800.
        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.solver.nx = 1
        self.solver.ny = 1
        su = self.solver.set_initial_condition()
        self.assertAlmostEqual(su, u, 0.1)
