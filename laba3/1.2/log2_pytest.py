import pytest
from log import calculator, convert_precision

def test_convert_precisision():
    assert convert_precision(1e-6) == 6
    assert convert_precision(1e-4) == 4
    assert convert_precision(1e-1) == 1

    with pytest.raises(ValueError, match = "Толерантность должна быть больше 0"):
        convert_precision(0)
    
    with pytest.raises(ValueError, match = "Толерантность должна быть больше 0"):
        convert_precision(-1e-6)

def test_calculator_arithmetic():
    assert calculator("+", 1.123456, 2.654321, tolerance = 1e-6) == 3.777777
    assert calculator("-", 1.123456, 2.654321, tolerance = 1e-6) == -1.530865
    assert calculator("*", 2, 3, tolerance = 1e-3) == 6.0
    assert calculator("/", 5, 2, tolerance = 1e-2) == 2.5
    assert calculator("/", 1, 0, tolerance = 1e-6) == "Я запрещаю делить на ноль"
    assert calculator("%", 1, 1, tolerance = 1e-6) == "Неизвестная команда"
    assert calculator("+", 1.1234567, 2.1234567) == round(3.2469134, 6)

def test_calculator_statistical():
    assert calculator("medium", 1, 2, 3, 4, tolerance=1e-6) == 2.5
    assert calculator("variance", 1, 2, 3, 4, tolerance =1e-6) == 1.666667
    assert calculator("std_deviation", 1, 2, 3, 4, tolerance = 1e-6) == 1.290994
    assert calculator("median", 1, 2, 3, 4, tolerance = 1e-6) == 2.5
    assert calculator("q3-q1", 1, 2, 3, 4, tolerance = 1e-6) == 2.0

    with pytest.raises(statistics.StatisticsError):
        calculator("variance", 1, tolerance = 1e-6)
    
    with pytest.raises(statistics.StatisticsError):
        calculator("std_deviation", 1, tolerance = 1e-6)

def test_calculator_invalid_inputs():
    assert calculator("+") == 0
    assert calculator("-", 1) == 1
    assert calculator("unknown_task", 1, 2) == "Неизвестная команда"

    with pytest.raises(TypeError):
        calculator("+", "a", "b")