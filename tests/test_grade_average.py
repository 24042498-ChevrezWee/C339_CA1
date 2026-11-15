import pytest
from src.grade_average import calculate_average

@pytest.mark.parametrize(
    ("mark_one", "mark_two", "expected"),
    [
        (0, 0, 0.0), # both lowest scores
        (100, 100, 100.0), # both highest scores
        (50, 50, 50.0), # both equal scores
        (0, 100, 50.0), # one mark at lowest score, one at highest score
        (100, 0, 50.0), # one mark at highest score, one at lowest score
        (40, 60, 50.0), # both normal scores
        (50, 51, 50.5), # test for average with decimal
        (0, 1, 0.5), # one mark at lowest score, one just above lowest score
        (99, 100, 99.5), # one mark just below highest score, one at highest score
    ],
)

def test_valid_marks_returns_expected_average(mark_one, mark_two, expected):
    # Act
    result = calculate_average(mark_one, mark_two)

    # Assert
    assert result == expected

@pytest.mark.parametrize(
    ("invalid_mark_type"),
    [
        ("a"), # string
        (None), # NoneType
        (50.5), # float
        ([50]), # list
        ({"mark": 50}), # dictionary
        ((50, 50)), # tuple
        (True), # boolean
        (False) # boolean
    ],
)

def test_invalid_mark_one_type_raises_type_error(invalid_mark_type):
    with pytest.raises(TypeError):
        calculate_average(invalid_mark_type, 50)

@pytest.mark.parametrize(
    ("invalid_mark_type"),
    [
        ("a"), # string
        (None), # NoneType
        (50.5), # float
        ([50]), # list
        ({"mark": 50}), # dictionary
        ((50, 50)), # tuple
        (True), # boolean
        (False) # boolean
    ],
)

def test_invalid_mark_two_type_raises_type_error(invalid_mark_type):
    with pytest.raises(TypeError):
        calculate_average(50, invalid_mark_type)

@pytest.mark.parametrize(
    ("invalid_mark_value"),
    [
        (-1), # below lower score
        (101) # above upper score
    ],
)

def test_invalid_mark_one_value_raises_value_error(invalid_mark_value):
    with pytest.raises(ValueError):
        calculate_average(invalid_mark_value, 50)

@pytest.mark.parametrize(
    ("invalid_mark_value"),
    [
        (-1), # below lower score
        (101) # above upper score
    ],
)

def test_invalid_mark_two_value_raises_value_error(invalid_mark_value):
    with pytest.raises(ValueError):
        calculate_average(50, invalid_mark_value)