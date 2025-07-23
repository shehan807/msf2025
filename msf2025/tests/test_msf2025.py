"""
Unit and regression test for the msf2025 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np
import msf2025


def test_msf2025_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "msf2025" in sys.modules


def test_calculate_angle():
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_value = 90

    output = msf2025.calculate_angle(r1, r2, r3, degrees=True)
    assert output == expected_value


def test_build_bond_list():
    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )
    bonds = msf2025.test_build_bond_list(coordinates)

    assert len(bonds) == 4
    for bond_length in bonds.values():
        assert bond_length == 1.4
