# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyPhonixJP/blob/main/LICENSE

from dataclasses import dataclass


@dataclass
class Word(object):
    spell: str
    kana: str


def convert2kana(raw: str, word_table: list[Word]):
    tmp = raw
    for word in word_table:
        tmp = tmp.replace(word.spell, word.kana)
    return tmp


def sort_by_spell_len_descending(wordlist: list[Word]):
    """pairlistのspellの文字数降順にソートする。副作用あり。"""
    wordlist.sort(key=lambda x: -len(x.spell))


def update_list(pairlist: list[Word], spell: str, kana: str, *, sort: bool = True):
    """pairlistのspellに対応するkanaが変更される。副作用あり。

    Args:
        pairlist (List[Word]): 変換表(変更される。)
        spell (str): 綴り
        kana (str): 読み
        sort (bool): pairlistをソートするか。spellの長い方から一致確認するために基本的にソートを行う。
    """
    spell = spell.lower()
    for i, pair in enumerate(pairlist):
        if pair.spell == spell:
            pairlist[i] = Word(spell, kana)
            break
    else:
        pairlist.append(Word(spell, kana))

        if sort:
            sort_by_spell_len_descending(pairlist)
