from main import is_valid

import pytest


@pytest.mark.parametrize("password, expected_valid", [
    ('122345', True),
    ('111123', True),
    ('135679', False),
    ('111111', True),
    ('223450', False),
    ('123789', False),
])
def test_is_valid(password, expected_valid):
    assert is_valid(password) == expected_valid


@pytest.mark.parametrize("password, expected_valid", [
    ('112233', True),
    ('123444', False),
    ('111122', True),
])
def test_is_valid_only_doubles(password, expected_valid):
    assert is_valid(password, exact_double=True) == expected_valid
