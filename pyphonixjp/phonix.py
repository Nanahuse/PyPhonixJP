# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyPhonixJP/blob/main/LICENSE

import re

from .common import convert2kana
from .conversion_table import VOWEL_ONN, PAIRS_PHONIX, PAIRS_PRONUNCIATION, CONSONANT_SIMPE


# 英単語の判別
RE_ALPHAVET = re.compile("[a-zA-Z]+")

# マジックEの変換定義
MAJIC_E = re.compile("[aeiou][^aeiou]e$")


def convert(word: str) -> str | None:
    """
    英単語の読みをphonixを活用してそれっぽいカタカナに変換する
    英単語ではない言葉が来るとNoneを返す。

    Args:
        word (str): 変換する英単語。半角英。

    Returns:
        Optional[str]: 単語のカタカナ読み
    """
    if RE_ALPHAVET.fullmatch(word) is None:
        return None
    raw = word.lower()

    # マジックE
    conv = MAJIC_E.search(raw)
    if conv is not None:
        conv = raw[: conv.start(0)] + VOWEL_ONN[raw[conv.start(0)]] + raw[conv.start(0) + 1]
    else:
        conv = raw

    # PHONIXの発音規則の適用
    conv = convert2kana(conv, PAIRS_PHONIX)
    conv = conv.lower()  # 変換の影響で大文字になっている部分があるので戻す

    conv = conv.replace("nn", "ン")

    # 促音の処理
    for spell in CONSONANT_SIMPE:
        while True:
            rep = conv.replace(f"{spell}{spell}", f"ッ{spell}")
            if rep == conv:
                break
            conv = rep

    # 発音処理
    conv = convert2kana(conv, PAIRS_PRONUNCIATION)

    return conv
