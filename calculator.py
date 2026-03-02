"""シンプルな電卓モジュール"""

import math


class Calculator:
    """基本的な四則演算と拡張関数を提供する電卓クラス"""

    def __init__(self) -> None:
        """電卓の初期化（計算履歴リストを生成）"""
        self._history: list[float | int] = []

    def add(self, a: float, b: float) -> float:
        """足し算"""
        result = a + b
        self._history.append(result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """引き算"""
        result = a - b
        self._history.append(result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """掛け算"""
        result = a * b
        self._history.append(result)
        return result

    def divide(self, a: float, b: float) -> float:
        """割り算（ゼロ除算時はValueError）"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        result = a / b
        self._history.append(result)
        return result

    def power(self, base: float, exponent: float) -> float:
        """累乗（base の exponent 乗）"""
        result = base ** exponent
        self._history.append(result)
        return result

    def sqrt(self, n: float) -> float:
        """平方根（負の数の場合はValueError）"""
        if n < 0:
            raise ValueError("負の数の平方根は計算できません")
        result = math.sqrt(n)
        self._history.append(result)
        return result

    def factorial(self, n: int) -> int:
        """階乗（負の整数の場合はValueError）"""
        if n < 0:
            raise ValueError("負の整数の階乗は計算できません")
        result = math.factorial(n)
        self._history.append(result)
        return result

    def history(self) -> list[float | int]:
        """計算履歴を返す（全ての演算結果を記録）"""
        return list(self._history)
