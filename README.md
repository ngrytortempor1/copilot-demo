# コピロットデモ

Copilot Coding Agent のデモ用リポジトリ。

## 概要
シンプルな電卓モジュール。基本的な四則演算と、拡張関数を提供する。

## 使い方
```python
from calculator import Calculator

calc = Calculator()
calc.add(2, 3)  # => 5
```

## テスト
```bash
python -m pytest tests/
```
