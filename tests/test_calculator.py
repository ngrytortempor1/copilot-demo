"""電卓モジュールの既存テスト（実装済み関数用）"""
import pytest
from calculator import Calculator


class TestCalculatorBasics:
    """基本的な四則演算のテスト"""

    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="ゼロで割ることはできません"):
            self.calc.divide(1, 0)


class TestCalculatorExtended:
    """拡張関数（power, sqrt, factorial, history）のテスト"""

    def setup_method(self):
        self.calc = Calculator()

    # --- power ---
    def test_power_positive(self):
        assert self.calc.power(2, 10) == 1024
        assert self.calc.power(3, 3) == 27

    def test_power_zero_exponent(self):
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(0, 0) == 1

    # --- sqrt ---
    def test_sqrt_normal(self):
        assert self.calc.sqrt(9) == pytest.approx(3.0)
        assert self.calc.sqrt(2) == pytest.approx(1.4142135623730951)

    def test_sqrt_negative_raises(self):
        with pytest.raises(ValueError, match="負の数の平方根は計算できません"):
            self.calc.sqrt(-1)

    # --- factorial ---
    def test_factorial_normal(self):
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(0) == 1

    def test_factorial_negative_raises(self):
        with pytest.raises(ValueError, match="負の整数の階乗は計算できません"):
            self.calc.factorial(-3)

    # --- history ---
    def test_history_records_results(self):
        self.calc.add(1, 2)       # 3
        self.calc.subtract(5, 1)  # 4
        self.calc.multiply(2, 3)  # 6
        self.calc.divide(10, 2)   # 5.0
        assert self.calc.history() == [3, 4, 6, 5.0]

    def test_history_includes_extended_functions(self):
        self.calc.power(2, 3)    # 8
        self.calc.sqrt(4)        # 2.0
        self.calc.factorial(3)   # 6
        assert self.calc.history() == [8, 2.0, 6]
