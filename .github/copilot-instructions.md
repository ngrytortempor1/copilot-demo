# プロジェクト概要
シンプルな電卓モジュール。基本的な四則演算と拡張関数を提供する Python ライブラリ。

# 技術スタック
- 言語: Python 3.12+
- テスト: pytest

# コーディング規約
- 関数にはdocstringを必ず書く
- 型ヒント（type hints）を必ず使う
- コメントとコミットメッセージは日本語で記述
- PEP 8 準拠

# モデル設定
- 使用モデル: **GPT-5.3-codex**
- 推論品質: **xhigh**（model_reasoning_effort: xhigh）

# テストコマンド
- テスト実行: `python -m pytest tests/ -v`

# 禁止事項
- 外部ライブラリの追加（標準ライブラリのみ使用すること。math モジュールはOK）
- 既存テストの削除・変更
- calculator.py の既存の実装済み関数（add, subtract, multiply, divide）のインターフェースを変更しないこと
