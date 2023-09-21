# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyPhonixJP/blob/main/LICENSE

from dataclasses import dataclass


@dataclass
class Word(object):
    spell: str
    kana: str


CONSONANT_SIMPE = "kstnhmyrwgzdbp"
VOWEL_ONN = {"a": "Eィ", "i": "Aィ", "u": "Uー", "e": "Iー", "o": "Oォ"}

# 発音規則の定義
PAIRS_PRONUNCIATION = [
    Word(spell="cha", kana="チャ"),
    Word(spell="chi", kana="チ"),
    Word(spell="chu", kana="チュ"),
    Word(spell="che", kana="チェ"),
    Word(spell="cho", kana="チョ"),
    Word(spell="sha", kana="シャ"),
    Word(spell="shi", kana="シ"),
    Word(spell="shu", kana="シュ"),
    Word(spell="she", kana="シェ"),
    Word(spell="sho", kana="ショ"),
    Word(spell="kya", kana="キャ"),
    Word(spell="kyi", kana="キィ"),
    Word(spell="kyu", kana="キュ"),
    Word(spell="kye", kana="キェ"),
    Word(spell="kyo", kana="キョ"),
    Word(spell="sya", kana="シャ"),
    Word(spell="syi", kana="シィ"),
    Word(spell="syu", kana="シュ"),
    Word(spell="sye", kana="シェ"),
    Word(spell="syo", kana="ショ"),
    Word(spell="tya", kana="チャ"),
    Word(spell="tyi", kana="チィ"),
    Word(spell="tyu", kana="チュ"),
    Word(spell="tye", kana="チェ"),
    Word(spell="tyo", kana="チョ"),
    Word(spell="nya", kana="ニャ"),
    Word(spell="nyi", kana="ニィ"),
    Word(spell="nyu", kana="ニュ"),
    Word(spell="nye", kana="ニェ"),
    Word(spell="nyo", kana="ニョ"),
    Word(spell="hya", kana="ヒャ"),
    Word(spell="hyi", kana="ヒィ"),
    Word(spell="hyu", kana="ヒュ"),
    Word(spell="hye", kana="ヒェ"),
    Word(spell="hyo", kana="ヒョ"),
    Word(spell="mya", kana="ミャ"),
    Word(spell="myi", kana="ミィ"),
    Word(spell="myu", kana="ミュ"),
    Word(spell="mye", kana="ミェ"),
    Word(spell="myo", kana="ミョ"),
    Word(spell="rya", kana="リャ"),
    Word(spell="ryi", kana="リィ"),
    Word(spell="ryu", kana="リュ"),
    Word(spell="rye", kana="リェ"),
    Word(spell="ryo", kana="リョ"),
    Word(spell="gya", kana="ギャ"),
    Word(spell="gyi", kana="ギィ"),
    Word(spell="gyu", kana="ギュ"),
    Word(spell="gye", kana="ギェ"),
    Word(spell="gyo", kana="ギョ"),
    Word(spell="zya", kana="ジャ"),
    Word(spell="zyi", kana="ジィ"),
    Word(spell="zyu", kana="ジュ"),
    Word(spell="zye", kana="ジェ"),
    Word(spell="zyo", kana="ジョ"),
    Word(spell="dya", kana="ヂャ"),
    Word(spell="dyi", kana="ヂィ"),
    Word(spell="dyu", kana="ヂュ"),
    Word(spell="dye", kana="ヂェ"),
    Word(spell="dyo", kana="ヂョ"),
    Word(spell="bya", kana="ビャ"),
    Word(spell="byi", kana="ビィ"),
    Word(spell="byu", kana="ビュ"),
    Word(spell="bye", kana="ビ ェ"),
    Word(spell="byo", kana="ビョ"),
    Word(spell="pya", kana="ピャ"),
    Word(spell="pyi", kana="ピィ"),
    Word(spell="pyu", kana="ピュ"),
    Word(spell="pye", kana="ピェ"),
    Word(spell="pyo", kana="ピョ"),
    Word(spell="va", kana="ヴァ"),
    Word(spell="vi", kana="ヴ ィ"),
    Word(spell="vu", kana="ヴゥ"),
    Word(spell="ve", kana="ヴェ"),
    Word(spell="vo", kana="ヴォ"),
    Word(spell="qa", kana="キァ"),
    Word(spell="qi", kana="キィ"),
    Word(spell="qu", kana="ク"),
    Word(spell="qe", kana="キェ"),
    Word(spell="qo", kana="キォ"),
    Word(spell="ja", kana="ジャ"),
    Word(spell="ji", kana="ジ"),
    Word(spell="ju", kana="ジュ"),
    Word(spell="je", kana="ジェ"),
    Word(spell="jo", kana="ジョ"),
    Word(spell="tsu", kana="ツ"),
    Word(spell="per", kana="パー"),
    Word(spell="ka", kana="カ"),
    Word(spell="ki", kana="キ"),
    Word(spell="ku", kana="ク"),
    Word(spell="ke", kana="ケ"),
    Word(spell="ko", kana="コ"),
    Word(spell="sa", kana="サ"),
    Word(spell="si", kana="シ"),
    Word(spell="su", kana="ス"),
    Word(spell="se", kana="セ"),
    Word(spell="so", kana="ソ"),
    Word(spell="ta", kana="タ"),
    Word(spell="ti", kana="チ"),
    Word(spell="tu", kana="ツ"),
    Word(spell="te", kana="テ"),
    Word(spell="to", kana="ト"),
    Word(spell="na", kana="ナ"),
    Word(spell="ni", kana="ニ"),
    Word(spell="nu", kana="ヌ"),
    Word(spell="ne", kana="ネ"),
    Word(spell="no", kana="ノ"),
    Word(spell="ha", kana="ハ"),
    Word(spell="hi", kana="ヒ"),
    Word(spell="hu", kana="フ"),
    Word(spell="he", kana="ヘ"),
    Word(spell="ho", kana="ホ"),
    Word(spell="ma", kana="マ"),
    Word(spell="mi", kana="ミ"),
    Word(spell="mu", kana="ム"),
    Word(spell="me", kana="メ"),
    Word(spell="mo", kana="モ"),
    Word(spell="ya", kana="ヤ"),
    Word(spell="yu", kana="ユ"),
    Word(spell="yo", kana="ヨ"),
    Word(spell="ra", kana="ラ"),
    Word(spell="ri", kana="リ"),
    Word(spell="ru", kana="ル"),
    Word(spell="re", kana="レ"),
    Word(spell="ro", kana="ロ"),
    Word(spell="wa", kana="ワ"),
    Word(spell="wi", kana="ヰ"),
    Word(spell="we", kana="ヱ"),
    Word(spell="wo", kana="ヲ"),
    Word(spell="ga", kana="ガ"),
    Word(spell="gi", kana="ギ"),
    Word(spell="gu", kana="グ"),
    Word(spell="ge", kana="ゲ"),
    Word(spell="go", kana="ゴ"),
    Word(spell="za", kana="ザ"),
    Word(spell="zi", kana="ジ"),
    Word(spell="zu", kana="ズ"),
    Word(spell="ze", kana="ゼ"),
    Word(spell="zo", kana="ゾ"),
    Word(spell="da", kana="ダ"),
    Word(spell="di", kana="ヂ"),
    Word(spell="du", kana="ヅ"),
    Word(spell="de", kana="デ"),
    Word(spell="do", kana="ド"),
    Word(spell="ba", kana="バ"),
    Word(spell="bi", kana="ビ"),
    Word(spell="bu", kana="ブ"),
    Word(spell="be", kana="ベ"),
    Word(spell="bo", kana="ボ"),
    Word(spell="pa", kana="パ"),
    Word(spell="pi", kana="ピ"),
    Word(spell="pu", kana="プ"),
    Word(spell="pe", kana="ペ"),
    Word(spell="po", kana="ポ"),
    Word(spell="la", kana="ラ"),
    Word(spell="li", kana="リ"),
    Word(spell="lu", kana="ル"),
    Word(spell="le", kana="レ"),
    Word(spell="lo", kana="ロ"),
    Word(spell="fa", kana="ファ"),
    Word(spell="fi", kana="フィ"),
    Word(spell="fu", kana="ヒュゥ"),
    Word(spell="fe", kana="フェ"),
    Word(spell="fo", kana="フォ"),
    Word(spell="ca", kana="キャ"),
    Word(spell="ci", kana="シ"),
    Word(spell="cu", kana="キュ"),
    Word(spell="ce", kana="セ"),
    Word(spell="co", kana="コ"),
    Word(spell="xa", kana="クサ"),
    Word(spell="xi", kana="クシ"),
    Word(spell="xu", kana="クス"),
    Word(spell="xe", kana="クセ"),
    Word(spell="xo", kana="クソ"),
    Word(spell="a", kana="ア"),
    Word(spell="i", kana="イ"),
    Word(spell="u", kana="ウ"),
    Word(spell="e", kana="エ"),
    Word(spell="o", kana="オ"),
    Word(spell="sh", kana="シュ"),
    Word(spell="ch", kana="チ"),
    Word(spell="b", kana="ブ"),
    Word(spell="c", kana="ク"),
    Word(spell="d", kana="ド"),
    Word(spell="f", kana="フ"),
    Word(spell="g", kana="グ"),
    Word(spell="h", kana="フ"),
    Word(spell="j", kana="ジ"),
    Word(spell="k", kana="ク"),
    Word(spell="l", kana="ル"),
    Word(spell="m", kana="ム"),
    Word(spell="n", kana="ン"),
    Word(spell="p", kana="プ"),
    Word(spell="q", kana="ク"),
    Word(spell="r", kana="ア"),
    Word(spell="s", kana="ス"),
    Word(spell="t", kana="ト"),
    Word(spell="v", kana="ブ"),
    Word(spell="w", kana="ウ"),
    Word(spell="x", kana="クス"),
    Word(spell="y", kana="イ"),
    Word(spell="z", kana="ズ"),
]

# 特別な発音規則の定義
PAIRS_PHONIX = [
    Word(spell="air", kana="Eイァ"),
    Word(spell="ald", kana="Eィルド"),
    Word(spell="and", kana="Eィンド"),
    Word(spell="ear", kana="Iアァ"),
    Word(spell="eld", kana="Iールド"),
    Word(spell="end", kana="Iーンド"),
    Word(spell="ild", kana="Aィルド"),
    Word(spell="ind", kana="Aィンド"),
    Word(spell="old", kana="Oォルド"),
    Word(spell="ond", kana="Oォンド"),
    Word(spell="spr", kana="スP"),
    Word(spell="str", kana="ストR"),
    Word(spell="thr", kana="スR"),
    Word(spell="uld", kana="Uールド"),
    Word(spell="und", kana="Uーンド"),
    Word(spell="wor", kana="ワー"),
    Word(spell="ai", kana="Eィ"),
    Word(spell="al", kana="Oー"),
    Word(spell="ar", kana="Aー"),
    Word(spell="au", kana="Oォ"),
    Word(spell="aw", kana="Oォ"),
    Word(spell="ay", kana="Eィ"),
    Word(spell="bl", kana="ブL"),
    Word(spell="br", kana="ブR"),
    Word(spell="ck", kana="K"),
    Word(spell="cl", kana="クL"),
    Word(spell="cr", kana="クR"),
    Word(spell="dr", kana="ドR"),
    Word(spell="ea", kana="Iー"),
    Word(spell="ee", kana="Iー"),
    Word(spell="ey", kana="Iー"),
    Word(spell="fl", kana="フL"),
    Word(spell="fr", kana="フR"),
    Word(spell="gl", kana="グL"),
    Word(spell="gr", kana="グR"),
    Word(spell="ie", kana="Aィ"),
    Word(spell="ir", kana="Aー"),
    Word(spell="ng", kana="ング"),
    Word(spell="oi", kana="Oイ"),
    Word(spell="oo", kana="Uゥ"),
    Word(spell="or", kana="Oー"),
    Word(spell="ow", kana="Aウ"),
    Word(spell="oy", kana="Oイ"),
    Word(spell="ph", kana="F"),
    Word(spell="pl", kana="プL"),
    Word(spell="sk", kana="スk"),
    Word(spell="sl", kana="スL"),
    Word(spell="sm", kana="スm"),
    Word(spell="sn", kana="スn"),
    Word(spell="sp", kana="スp"),
    Word(spell="st", kana="スt"),
    Word(spell="sw", kana="スw"),
    Word(spell="th", kana="S"),
    Word(spell="tr", kana="トR"),
    Word(spell="ui", kana="Uー"),
    Word(spell="wh", kana="W"),
]
