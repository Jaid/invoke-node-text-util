import re
import unicodedata

def isCharacterPrintable(c: str) -> bool:
  if ord(c) == 0x200B: # Zero-width space
    return False
  if ord(c) == 0x200C: # Zero-width non-joiner
    return False
  if ord(c) == 0x200D: # Zero-width joiner
    return False
  if ord(c) == 0x000A: # Line feed
    return True
  category = unicodedata.category(c)
  if category == 'Cc': # Control characters
    return False
  return True

def strip(text: str) -> str:
  text = text.strip()
  return text

def stripLineEndings(text: str) -> str:
  text = re.sub(r'([^\S\n]+)$', '', text)
  return text

def stripLineStarts(text: str) -> str:
  text = re.sub(r'^([^\S\n]+)', '', text)
  return text

def normalizeLineEndings(text: str) -> str:
  text = re.sub(r'\r\n', '\n', text)
  text = re.sub(r'\r', '\n', text)
  return text

def compressWhitespace(text: str) -> str:
  text = re.sub(r'[^\S\n]+', ' ', text)
  return text

def normalizeUnicode(text: str, unicodeNormalizeCategory: str = 'NFKC') -> str:
  text = unicodedata.normalize(unicodeNormalizeCategory, text)
  return text

def clearUnprintable(text: str) -> str:
  text = ''.join(filter(isCharacterPrintable, text))
  return text

def compressCommas(text: str) -> str:
  text = re.sub(r"\s*,[\s,]*,\s*", ", ", text)
  return text

def trimBeforeCommas(text: str) -> str:
  text = re.sub(r'\s+,', ',', text)
  return text

def compressLines(text: str, joiner: str = " ") -> str:
  text = re.sub("\n+", joiner, text)
  return text
