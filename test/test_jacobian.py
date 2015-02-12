'''Test jacobian formation.'''
import pytest
from fe_utils import UnitIntervalMesh, UnitSquareMesh
import numpy as np


def test_jacobian_type_1d():

    m = UnitIntervalMesh(2)

    J = m.jacobian(1)

    assert isinstance(J, np.ndarray), \
        "Jacobian must be a numpy array, not a %s" % type(J)


def test_jacobian_type_2d():

    m = UnitSquareMesh(2, 2)

    J = m.jacobian(1)

    assert isinstance(J, np.ndarray), \
        "Jacobian must be a numpy array, not a %s" % type(J)


def test_jacobian_shape_1d():

    m = UnitIntervalMesh(2)

    J = m.jacobian(1)

    assert J.shape == (1, 1), \
        "Jacobian must have shape (1, 1), not %s" % str(J.shape)


def test_jacobian_shape_2d():

    m = UnitSquareMesh(2, 2)

    J = m.jacobian(1)

    assert J.shape == (2, 2), \
        "Jacobian must have shape (2, 2), not %s" % str(J.shape)


def test_jacobian_1d():

    m = UnitIntervalMesh(2)

    assert (np.linalg.det(m.jacobian(1)) - .5).round() == 0


def test_jacobian_2d():

    m = UnitSquareMesh(2, 2)

    assert (np.linalg.det(m.jacobian(1)) - .125).round() == 0