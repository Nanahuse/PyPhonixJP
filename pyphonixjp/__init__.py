# Copyright (c) 2023 Nanahuse
# This software is released under the MIT License
# https://github.com/Nanahuse/PyPhonixJP/blob/main/LICENSE

# flake8: noqa

from .conversion_table import PAIRS_PHONIX, PAIRS_PRONUNCIATION
from .phonix import convert

__all__ = ["convert", "PAIRS_PHONIX", "PAIRS_PRONUNCIATION"]
