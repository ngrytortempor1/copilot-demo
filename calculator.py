"""シンプルな電卓モジュール"""


class Calculator:
    """基本的な四則演算と拡張関数を提供する電卓クラス"""

    def add(self, a: float, b: float) -> float:
        """足し算"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """引き算"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """掛け算"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """割り算（ゼロ除算時はValueError）"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        return a / b

    # TODO: 以下の関数は未実装
    # Copilot Agentに実装を委譲する

    def power(self, base: float, exponent: float) -> float:
        """累乗（base の exponent 乗）"""
        raise NotImplementedError("この関数は未実装です")

    def sqrt(self, n: float) -> float:
        """平方根（負の数の場合はValueError）"""
        raise NotImplementedError("この関数は未実装です")

    def factorial(self, n: int) -> int:
        """階乗（負の整数の場合はValueError）"""
        raise NotImplementedError("この関数は未実装です")

    def history(self) -> list:
        """計算履歴を返す（全ての演算結果を記録）"""
        raise NotImplementedError("この関数は未実装です")
