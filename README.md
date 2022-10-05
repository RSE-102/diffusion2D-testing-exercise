# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/RSE-102/Lecture-Material/blob/main/04_testing/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
========================================== test session starts ===========================================
platform linux -- Python 3.7.5, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/mugurlu/Git_Repositories/diffusion2D-testing-exercise
collected 5 items                                                                                        

tests/integration/test_diffusion2d.py ..                                                           [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                       [100%]

================================================ FAILURES ================================================
_________________________________________ test_initialize_domain _________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(20.,20.,1.,1.)
>       assert solver.nx == 20+1
E       assert 20 == (20 + 1)
E        +  where 20 = <diffusion2d.SolveDiffusion2D object at 0x7fbeb4d8b510>.nx

tests/unit/test_diffusion2d_functions.py:15: AssertionError
__________________________________ test_initialize_physical_parameters ___________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        # solver.initialize_domain(20.,20.,1.,1.)
        solver.dx = 1.
        solver.dy = 1.
        solver.initialize_physical_parameters(5., 200., 500.)
        expected_dt = pytest.approx(0.05+1, rel=1e-6)
>       assert solver.dt == expected_dt
E       assert 0.05 == 1.05 ± 1.0e-06
E         comparison failed
E         Obtained: 0.05
E         Expected: 1.05 ± 1.0e-06

tests/unit/test_diffusion2d_functions.py:29: AssertionError
------------------------------------------ Captured stdout call ------------------------------------------
dt = 0.05
_______________________________________ test_set_initial_condition _______________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        # solver.initialize_domain(30.,30.,10.,10.)
        # solver.initialize_physical_parameters(5., 200., 500.)
        solver.dx = 10.
        solver.dy = 10.
        solver.T_cold = 200.
        solver.T_hot = 500.
        solver.nx = 3+3
        solver.ny = 3
        u0 = solver.set_initial_condition()
        expected_u0 = pytest.approx(np.array([[200., 200., 200.],[200., 200., 200.],[200., 200., 200.]]), rel=1e-6)
>       assert u0 == expected_u0
E       assert array([[200.,... 200., 200.]]) == approx([[200....0 ± 2.0e-04]])
E         Impossible to compare arrays with different shapes.
E         Shapes: (3, 3) and (6, 3)

tests/unit/test_diffusion2d_functions.py:50: AssertionError
======================================== short test summary info =========================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 20 == (20 + 1)
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.05 == 1...
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert array([[200.,... 2...
====================================== 3 failed, 2 passed in 0.59s =======================================




========================================== test session starts ===========================================
platform linux -- Python 3.7.5, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/mugurlu/Git_Repositories/diffusion2D-testing-exercise
collected 5 items                                                                                        

tests/integration/test_diffusion2d.py FF                                                           [ 40%]
tests/unit/test_diffusion2d_functions.py ...                                                       [100%]

================================================ FAILURES ================================================
__________________________________ test_initialize_physical_parameters ___________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(20., 20., 1., 1.)
        solver.initialize_physical_parameters(5., 200., 500.)
        expected_dt = pytest.approx(0.05+1, rel=1e-2)
>       assert solver.dt == expected_dt
E       assert 0.05 == 1.05 ± 1.1e-02
E         comparison failed
E         Obtained: 0.05
E         Expected: 1.05 ± 1.1e-02

tests/integration/test_diffusion2d.py:18: AssertionError
------------------------------------------ Captured stdout call ------------------------------------------
dt = 0.05
_______________________________________ test_set_initial_condition _______________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_condition
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(30., 30., 10., 10.)
        solver.initialize_physical_parameters(5., 200., 500.)
        u0 = solver.set_initial_condition()
        expected_u0 = pytest.approx(np.array([[200.+100, 200., 200.],[200., 200., 200.],[200., 200., 200.]]), rel=1e-2)
>       assert u0 == expected_u0
E       assert array([[200.,... 200., 200.]]) == approx([[300....0 ± 2.0e+00]])
E         comparison failed. Mismatched elements: 1 / 9:
E         Max absolute difference: 100.0
E         Max relative difference: 0.5
E         Index  | Obtained | Expected       
E         (0, 0) | 200.0    | 300.0 ± 3.0e+00

tests/integration/test_diffusion2d.py:30: AssertionError
------------------------------------------ Captured stdout call ------------------------------------------
dt = 5.0
======================================== short test summary info =========================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.05 == 1.05...
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert array([[200.,... 200....
====================================== 2 failed, 3 passed in 0.61s =======================================


### unittest log
Fdt = 0.05
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mugurlu/Git_Repositories/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 35, in test_initialize_domain
    self.assertEqual(solver.nx, 20+1)
AssertionError: 20 != 21

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mugurlu/Git_Repositories/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 48, in test_initialize_physical_parameters
    self.assertAlmostEqual(solver.dt, expected_dt, 2)
AssertionError: 0.05 != 1.05 within 2 places (1.0 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/mugurlu/Git_Repositories/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 64, in test_set_initial_condition
    self.assertAlmostEqual(u0[0,0], expected_u0[0,0], 3)
AssertionError: 300.0 != 200.0 within 3 places (100.0 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
