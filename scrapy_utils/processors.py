'''
Processors seen in former scrapylib

'''
import re

from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.utils.markup import (remove_tags, replace_escape_chars, unquote_markup)

_clean_spaces_re = re.compile(r'\s+', re.U)
_br_re = re.compile(r'<br\s?\/?>', re.IGNORECASE)


def clean_spaces(value):
    return _clean_spaces_re.sub(' ', value)


def replace_br(value):
    return _br_re.sub(' ', value)


def replace_escape(value):
    return replace_escape_chars(value, replace_by=u' ')


def split(value):
    return [v.strip() for v in value.split(',')]


def strip(value):
    return value.strip()


default_input_processor = MapCompose(
    replace_br, remove_tags, unquote_markup, replace_escape, strip, clean_spaces
)

default_output_processor = TakeFirst()
