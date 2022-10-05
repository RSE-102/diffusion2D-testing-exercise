# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/RSE-102/Lecture-Material/blob/main/04_testing/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 1.
        h = 2.
        dx = 0.5
        dy = 0.5
        nx = 2.
        ny = 4.
        solver.initialize_domain(w, h, dx, dy)
>       assert(solver.nx == nx)
E       assert 4 == 2.0
E        +  where 4 = <diffusion2d.SolveDiffusion2D object at 0x7f753045e580>.nx

tests/unit/test_diffusion2d_functions.py:20: AssertionError


### unittest log

======================================================================
ERROR: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/rwinter/DUMUX/Workshop_RSE102/diffusion2D-testing-exercise/tests/unit/test_diffusion2d_functions.py", line 24, in test_initialize_domain
    self.assertAlmostEqual(self.solver.nx, nx, 0.1)
  File "/usr/lib/python3.8/unittest/case.py", line 957, in assertAlmostEqual
    if round(diff, places) == 0:
TypeError: 'float' object cannot be interpreted as an integer

### integrationtest log

=========================================================================================== test session starts ===========================================================================================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/rwinter/DUMUX/Workshop_RSE102/diffusion2D-testing-exercise
collected 5 items                                                                                                                                                                                         

tests/integration/test_diffusion2d.py .F                                                                                                                                                            [ 40%]
tests/unit/test_diffusion2d_functions.py F..                                                                                                                                                        [100%]

================================================================================================ FAILURES =================================================================================================
_______________________________________________________________________________________ test_set_initial_condition ________________________________________________________________________________________

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
>       assert(np.allclose(su,u))

tests/integration/test_diffusion2d.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
<__array_function__ internals>:5: in allclose
    ???
/usr/lib/python3/dist-packages/numpy/core/numeric.py:2171: in allclose
    res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
<__array_function__ internals>:5: in isclose
    ???
/usr/lib/python3/dist-packages/numpy/core/numeric.py:2272: in isclose
    return within_tol(x, y, atol, rtol)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

x = array([[400., 400., 400., 400.],
       [400., 400., 400., 400.],
       [400., 400., 400., 400.],
       [400., 400., 400., 400.]])
y = array([[400., 400., 400., 400.],
       [400., 400., 400., 400.]]), atol = 1e-08, rtol = 1e-05

    def within_tol(x, y, atol, rtol):
        with errstate(invalid='ignore'):
>           return less_equal(abs(x-y), atol + rtol * abs(y))
E           ValueError: operands could not be broadcast together with shapes (4,4) (2,4)

/usr/lib/python3/dist-packages/numpy/core/numeric.py:2258: ValueError
------------------------------------------------------------------------------------------ Captured stdout call -------------------------------------------------------------------------------------------
dt = 0.03125
_________________________________________________________________________________ TestDiffusion2D.test_initialize_domain __________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

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
>       self.assertAlmostEqual(self.solver.nx, nx, 0.1)
E       TypeError: 'float' object cannot be interpreted as an integer

tests/unit/test_diffusion2d_functions.py:24: TypeError
========================================================================================= short test summary info =========================================================================================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - ValueError: operands could not be broadcast together with shapes (4,4) (2,4)
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - TypeError: 'float' object cannot be interpreted as an integer
======================================================================================= 2 failed, 3 passed in 0.68s =======================================================================================



## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
