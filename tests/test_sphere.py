"""
Mariana Samperio
639835

This test is based off of the test_box.py one
"""

import pytest
import math
from geometry.sphere import volume_sphere


def test_sphere_valid_inputs():
    """
    test volume for valid sphere radius
    """
    radius = 3.0
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == expected


def test_sphere_negative_radius():
    """
    testing that negative radius actually give ValueError
    """
    radius = -3.0
    with pytest.raises(ValueError):
        volume_sphere(radius)


def test_sphere_float_tolerance():
    radius = 1.1
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
