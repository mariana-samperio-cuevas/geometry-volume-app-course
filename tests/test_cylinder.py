"""
Mariana Samperio 
639835
   
This test is based off of the test_box.py one
"""


import pytest
import math
from geometry.cylinder import volume_cylinder


def test_cylinder_valid_inputs():
    """
    testing valid cylinder dimensions
    """
    radius, height = 3.0, 5.0
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == expected


def test_cylinder_negative_dimension():
    """
    testing when a negative dimension is used
    """
    radius, height = -3.0, 5.0
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == expected


def test_cylinder_float_tolerance():
    radius, height = 1.1, 2.2
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == pytest.approx(expected, rel=1e-6)
