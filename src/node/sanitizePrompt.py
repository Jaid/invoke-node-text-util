import functools

from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringOutput

from ...src.handler.sanitizePrompt import process

@invocation(
  'jaid/invoke-node-text-util/sanitizePrompt',
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
    'prompt',
  ],
  category='string',
  version='1.0.0',
)
class SanitizePromptInvocation(BaseInvocation):
  """Rewrites prompt to be a single line, cleans consecutive commas and sanitizes text"""

  text: str = InputField(
    title='Text',
    description='Input text',
  )
  commaOnLinebreak: bool = InputField(
    title='Comma on Linebreak',
    default=True,
    description='If true, inserts a comma at the places where linebreaks used to be. If false, lines are joined with a space.',
  )

  def invoke(self, context) -> StringOutput:
    output = process(self.text, self.commaOnLinebreak)
    return StringOutput(value=output)
