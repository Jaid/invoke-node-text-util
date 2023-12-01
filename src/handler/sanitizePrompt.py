import functools

from ..lib.sanitizeText import (
  compressWhitespace,
  normalizeUnicode,
  clearUnprintable,
  strip,
  compressCommas,
  compressLines,
)

def process(text: str, commaOnLinebreak: bool) -> str:
  text = functools.reduce(lambda acc, fn: fn(acc), [
    compressWhitespace,
    normalizeUnicode,
    clearUnprintable,
    strip,
    compressLines if commaOnLinebreak else functools.partial(compressLines, joiner=", "),
    compressCommas,
  ], text)
  return text
