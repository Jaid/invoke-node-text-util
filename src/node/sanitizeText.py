import functools

from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringOutput

from ...src.handler.sanitizeText import process

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
