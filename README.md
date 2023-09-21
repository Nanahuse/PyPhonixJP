# PyPhonixJP

英単語の読みをフォニックス（phonix）を用いてカタカナ英語に変換する。
綴りをもとに機械的に変換するだけであり実際の発音と異なる。

# Install
```
pip install pyphonixjp
```

# How to Use
```python
from pyphonixjp import convert, update_list, PAIRS_PHONIX, PAIRS_PRONUNCIATION

PAIRS_PHONIX # Phonix特有の母音や子音の変換表 変換優先度高
PAIRS_PRONUNCIATION # ローマ字読みや単体のアルファベットの変換表 変換優先度低

print(convert("pyphonixjp"))
# プイフォニクスジプ

update_list(PAIRS_PRONUNCIATION, "py", "パイ")
update_list(PAIRS_PRONUNCIATION, "jp", "ジェイピー")
print(convert("pyphonixjp"))
# パイフォニクスジェイピー
```

# How to convert
1. マジックEの変換
1. PHONIX規則に基づく変換（PAIRS_PHONIXを使用）
1. ローマ字読みやアルファベットの変換（PAIRS_PRONUNCIATIONを使用）
1. ローマ字読みやアルファベットの変換（PAIRS_PRONUNCIATIONを使用）2回目（1回では変換しきれないため）

# Lisence
MITライセンス  
詳しくは[LICENSE](./LICENSE)を確認ください。

