import functools

from ..lib import sanitizeText

def process(text: str) -> str:
  text = functools.reduce(lambda acc, fn: fn(acc), [
    sanitizeText.normalizeLineEndings,
    sanitizeText.strip,
    sanitizeText.stripLineEndings,
    sanitizeText.compressWhitespace,
    sanitizeText.normalizeUnicode,
    sanitizeText.clearUnprintable,
  ], text)
  return text
