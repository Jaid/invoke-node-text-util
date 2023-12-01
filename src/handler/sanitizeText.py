import functools

from ..lib import sanitizeText

def process(text: str) -> str:
  text = functools.reduce(lambda acc, fn: fn(acc), [
    sanitizeText.strip,
    sanitizeText.compressWhitespace,
    sanitizeText.normalizeUnicode,
    sanitizeText.clearUnprintable,
  ], text)
  return text
