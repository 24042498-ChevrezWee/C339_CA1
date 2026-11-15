import pytest
from src.grade_pass import has_passed

@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (0, False), # lowest score
        (1, False), # just above lowest score
        (49, False), # just below pass score
        (50, True), # exact pass score
        (51, True), # just above pass score
        (75, True), # normal pass score
        (99, True), # just below highest score
        (100, True) # highest score
    ],
)

def test_valid_score_returns_expected_result(score, expected):
    # Act
    result = has_passed(score)

    # Assert
    assert result is expected

@pytest.mark.parametrize(
    ("invalid_score_type"),
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

def test_invalid_score_type_raises_type_error(invalid_score_type):
    with pytest.raises(TypeError):
        has_passed(invalid_score_type)

@pytest.mark.parametrize(
    ("invalid_score_value"),
    [
        (-1), # below lowest score
        (101) # above highest score
    ],
)

def test_invalid_score_value_raises_value_error(invalid_score_value):
    with pytest.raises(ValueError):
        has_passed(invalid_score_value)