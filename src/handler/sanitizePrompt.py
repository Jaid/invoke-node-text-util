import functools

from ..lib import sanitizeText

def process(text: str, commaOnLinebreak: bool) -> str:
  text = functools.reduce(lambda acc, fn: fn(acc), [
    sanitizeText.normalizeLineEndings,
    functools.partial(sanitizeText.compressLines, joiner=", ") if commaOnLinebreak else sanitizeText.compressLines,
    sanitizeText.compressWhitespace,
    sanitizeText.normalizeUnicode,
    sanitizeText.clearUnprintable,
    sanitizeText.strip,
    sanitizeText.stripLineEndings,
    sanitizeText.stripLineStarts,
    sanitizeText.compressCommas,
    sanitizeText.trimBeforeCommas,
  ], text)
  return text
