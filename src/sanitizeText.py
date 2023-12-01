import re
import unicodedata

from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringOutput

def isCharacterPrintable(c: str) -> bool:
  category = unicodedata.category(c)
  if ord(c) == 0x200B: # Zero-width space
    return False
  if ord(c) == 0x200C: # Zero-width non-joiner
    return False
  if ord(c) == 0x200D: # Zero-width joiner
    return False
  if category == 'Cc': # Control characters
    return False
  return True

def process(text: str) -> str:
  unicodeNormalizeCategory = 'NFKC'
  text = text.strip()
  text = re.sub('\\s+', ' ', text)
  text = unicodedata.normalize(unicodeNormalizeCategory, text)
  text = ''.join(filter(isCharacterPrintable, text))
  return text

@invocation(
  'jaid/invoke-node-text-util/sanitizeText',
  title='Sanitize Text',
  tags=[
    'clean',
    'normalize',
    'sanitize',
    'simplify',
    'string',
    'strings',
    'text',
    'tidy',
    'trim',
    'whitespace',
  ],
  category='string',
  version='1.0.0',
)
class SanitizeTextInvocation(BaseInvocation):
  """Removes leading and trailing whitespace and invisible characters from the given text, compresses consecutive whitespace characters into a single space"""

  text: str = InputField(
    title='Text',
    description='Input text',
  )

  def invoke(self, context) -> StringOutput:
    output = process(self.text)
    return StringOutput(value=output)
