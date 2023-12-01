import functools

from ...src.lib.sanitizeText import *

def process(text: str) -> str:
  text = functools.reduce(lambda acc, fn: fn(acc), [
    strip,
    compressWhitespace,
    normalizeUnicode,
    clearUnprintable,
  ], text)
  return text
