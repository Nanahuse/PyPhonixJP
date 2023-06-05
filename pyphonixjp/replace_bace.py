# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyPhonixJP/blob/main/LICENSE

from dataclasses import dataclass
from typing import List


@dataclass
class WordPair(object):
    spell: str
    kana: str


def generate_letter_prefix(prefix: str, wordlist: List[str]):
    """前半を固定して末尾を入れ替えた文字列を作成する。

    Args:
        prefix (str): 前半部分の固定文字列
        wordlist (List[str]): 後半部分の入れ替える文字配列

    Returns:
        list[str]: 生成した文字列
    """
    return [prefix + tmp for tmp in wordlist]


def generate_letter_suffix(wordlist: List[str], suffix: str):
    """後半を固定して前半を入れ替えた文字列を作成する。

    Args:
        wordlist (List[str]): 前半部分の入れ替える文字配列
        suffix (str): _後半部分の固定文字列

    Returns:
        list[str]: 生成した文字列
    """
    return [tmp + suffix for tmp in wordlist]


def replace_spell2kana(raw: str, pairs: List[WordPair]):
    """WordPairのpairに設定されている文字をbaseへと変換する。

    Args:
        raw (str): 置換する文字列
        pairs (List[WordPair]): 対応表

    Returns:
        str: 置換後の文字列
    """
    tmp = raw
    for pair in pairs:
        tmp = tmp.replace(pair.spell, pair.kana)
    return tmp


def sort_by_spell_len_descending(pairlist: List[WordPair]):
    """pairlistのspellの文字数降順にソートする。副作用あり。"""
    pairlist.sort(key=lambda x: -len(x.spell))


def update_list(pairlist: List[WordPair], spell: str, kana: str, *, sort: bool = True):
    """pairlistのspellに対応するkanaが変更される。副作用あり。

    Args:
        pairlist (List[WordPair]): 変換表(変更される。)
        spell (str): 綴り
        kana (str): 読み
        sort (bool): pairlistをソートするか。spellの長い方から一致確認するために基本的にソートを行う。
    """
    spell = spell.lower()
    for i, pair in enumerate(pairlist):
        if pair.spell == spell:
            pairlist[i] = WordPair(spell, kana)
            break
    else:
        pairlist.append(WordPair(spell, kana))

        if sort:
            sort_by_spell_len_descending(pairlist)
