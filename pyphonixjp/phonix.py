# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyPhonixJP/blob/main/LICENSE

import itertools
from typing import List, Optional
import re
from pyphonixjp.replace_bace import (
    WordPair,
    generate_letter_prefix,
    replace_spell2kana,
    update_list,
    sort_by_spell_len_descending,
)

VOWEL = "aiueo"  # 母音一覧
CONSONANT_SIMPE = "kstnhmyrwgzdbp"  # 子音一覧
VOWEL_ONN = {"a": "Eィ", "i": "Aィ", "u": "Uー", "e": "Iー", "o": "Oォ"}  # 母音の読み方


class KATAKANA:
    A = "アイウエオ"
    K = "カキクケコ"
    S = "サシスセソ"
    T = "タチツテト"
    N = "ナニヌネノ"
    H = "ハヒフヘホ"
    M = "マミムメモ"
    Y = "ヤユヨ"
    R = "ラリルレロ"
    W = "ワヰヱヲ"
    NN = "ン"
    G = "ガギグゲゴ"
    Z = "ザジズゼゾ"
    D = "ダヂヅデド"
    B = "バビブベボ"
    P = "パピプペポ"
    V = "ヴ"
    A_SMALL = "ァィゥェォ"
    Y_SMALL = "ャィュェョ"
    T_SMALL = "ッ"


# アルファベットを見分ける正規表現
RE_ALPHAVET = re.compile("[a-zA-Z]*")

# マジックEの変換定義
MAJIC_E = re.compile("[aeiou][bcdfghjklmnpqrstvwxyz]e$")

# 特別な発音規則の定義
PAIRS_PHONIX: List[WordPair] = list(
    itertools.chain.from_iterable(
        [
            [WordPair(f"s{tmp}", f"ス{tmp}") for tmp in "mnkptw"],
            [WordPair(f"{tmp}l", f"{oto}l") for tmp, oto in zip("bpcgfs", "ブプクグフス")],
            [WordPair(f"{tmp}r", f"{oto}r") for tmp, oto in zip("bfcgdt", "ブフクグドト")],
            [WordPair(f"{tmp}r", f"{oto}r") for tmp, oto in zip(("thr", "spr", "str"), ("スR", "スP", "ストR"))],
            [WordPair("ar", "Aー")],
            [WordPair("or", "Oー")],
            [WordPair("ir", "Aー")],
            [WordPair("air", "Eイァ")],
            [WordPair("air", "Iアァ")],
            [WordPair("wor", "ワー")],
            [WordPair("al", "Oー")],
            [WordPair(f"{tmp}ld", f"{VOWEL_ONN[tmp]}ルド") for tmp in "aiueo"],
            [WordPair(f"{tmp}nd", f"{VOWEL_ONN[tmp]}ンド") for tmp in "aiueo"],
            [WordPair("oo", "Uゥ")],
            [WordPair(tmp, "Aウ") for tmp in ("oo", "ow")],
            [WordPair(tmp, "Oイ") for tmp in ("oi", "oy")],
            [WordPair(tmp, "Oォ") for tmp in ("au", "aw")],
            [WordPair("ph", "F")],
            [WordPair("wh", "W")],
            [WordPair("th", "S")],
            [WordPair("ck", "K")],
            [WordPair("ng", "ング")],
            [WordPair(tmp, VOWEL_ONN["a"]) for tmp in ("ai", "ay")],
            [WordPair(tmp, VOWEL_ONN["e"]) for tmp in ("ea", "ee", "ey")],
            [WordPair("ie", VOWEL_ONN["i"])],
            [WordPair("ow", VOWEL_ONN["o"])],
            [WordPair("ui", VOWEL_ONN["u"])],
        ]
    )
)
"""
Phonix独特の発音規則
"""
sort_by_spell_len_descending(PAIRS_PHONIX)  # スペルの長い方から一致確認するため降順に並べておく

# 通常の発音規則の定義
PAIRS_PRONUNCIATION: List[WordPair] = list(
    itertools.chain.from_iterable(
        [
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("ch", VOWEL),
                    generate_letter_prefix("チ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("sh", VOWEL),
                    generate_letter_prefix("シ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("ky", VOWEL),
                    generate_letter_prefix("キ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("sy", VOWEL),
                    generate_letter_prefix("シ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("ty", VOWEL),
                    generate_letter_prefix("チ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("ny", VOWEL),
                    generate_letter_prefix("ニ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("hy", VOWEL),
                    generate_letter_prefix("ヒ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("my", VOWEL),
                    generate_letter_prefix("ミ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("ry", VOWEL),
                    generate_letter_prefix("リ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("gy", VOWEL),
                    generate_letter_prefix("ギ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("zy", VOWEL),
                    generate_letter_prefix("ジ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("dy", VOWEL),
                    generate_letter_prefix("ヂ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("by", VOWEL),
                    generate_letter_prefix("ビ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("py", VOWEL),
                    generate_letter_prefix("ピ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("v", VOWEL),
                    generate_letter_prefix("ヴ", KATAKANA.A_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("q", VOWEL),
                    generate_letter_prefix("キ", KATAKANA.A_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("j", VOWEL),
                    generate_letter_prefix("ジ", KATAKANA.Y_SMALL),
                )
            ],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("f", VOWEL),
                    generate_letter_prefix("フ", KATAKANA.Y_SMALL),
                )
            ],
            [WordPair("tsu", "ツ")],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("k", VOWEL), KATAKANA.K)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("s", VOWEL), KATAKANA.S)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("t", VOWEL), KATAKANA.T)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("n", VOWEL), KATAKANA.N)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("h", VOWEL), KATAKANA.H)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("m", VOWEL), KATAKANA.M)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("y", "auo"), KATAKANA.Y)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("r", VOWEL), KATAKANA.R)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("w", "aieo"), KATAKANA.W)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("g", VOWEL), KATAKANA.G)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("z", VOWEL), KATAKANA.Z)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("d", VOWEL), KATAKANA.D)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("b", VOWEL), KATAKANA.B)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("p", VOWEL), KATAKANA.P)],
            [WordPair(spell, kana) for spell, kana in zip(generate_letter_prefix("l", VOWEL), KATAKANA.R)],
            [
                WordPair(spell, kana)
                for spell, kana in zip(
                    generate_letter_prefix("x", VOWEL),
                    generate_letter_prefix("ク", KATAKANA.S),
                )
            ],
            [WordPair(spell, kana) for spell, kana in zip(VOWEL, KATAKANA.A)],
            [
                WordPair("sh", "シュ"),
                WordPair("ch", "チ"),
                WordPair("b", "ブ"),
                WordPair("c", "ク"),
                WordPair("d", "ド"),
                WordPair("f", "フ"),
                WordPair("g", "ド"),
                WordPair("h", "フ"),
                WordPair("j", "ジ"),
                WordPair("k", "ク"),
                WordPair("l", "ル"),
                WordPair("m", "ム"),
                WordPair("n", "ン"),
                WordPair("p", "プ"),
                WordPair("q", "ク"),
                WordPair("r", "ア"),
                WordPair("s", "ス"),
                WordPair("t", "ト"),
                WordPair("v", "ブ"),
                WordPair("w", "ウ"),
                WordPair("x", "クス"),
                WordPair("y", "イ"),
                WordPair("z", "ズ"),
            ],
        ]
    )
)
"""
基本的な発音規則

ローマ字読みやアルファベット単体など
"""

# 規則的ではない変換部分を置き換える
update_list(PAIRS_PRONUNCIATION, "wi", "ウィ", sort=False)
update_list(PAIRS_PRONUNCIATION, "we", "ウェ", sort=False)
update_list(PAIRS_PRONUNCIATION, "chi", "チ", sort=False)
update_list(PAIRS_PRONUNCIATION, "shi", "シ", sort=False)
update_list(PAIRS_PRONUNCIATION, "fo", "フォ", sort=False)
update_list(PAIRS_PRONUNCIATION, "qu", "ク", sort=False)
update_list(PAIRS_PRONUNCIATION, "ji", "ジ", sort=False)
sort_by_spell_len_descending(PAIRS_PRONUNCIATION)


def convert(word: str) -> Optional[str]:
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
    # 入力は半角小文字にそろえる。
    raw = word.lower()
    conv = MAJIC_E.search(raw)
    if conv is not None:
        conv = raw[: conv.start(0)] + VOWEL_ONN[raw[conv.start(0)]] + raw[conv.start(0) + 1]
    else:
        conv = raw
    conv = replace_spell2kana(conv, PAIRS_PHONIX)
    conv = replace_spell2kana(conv.lower(), PAIRS_PRONUNCIATION)
    conv = conv.replace("nn", "ン")
    for tmp in CONSONANT_SIMPE:
        while True:
            rep = conv.replace(f"{tmp}{tmp}", f"ッ{tmp}")
            if rep == conv:
                break
            conv = rep
    conv = replace_spell2kana(conv, PAIRS_PRONUNCIATION)

    return conv
