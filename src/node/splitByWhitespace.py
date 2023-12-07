from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringCollectionOutput

from ..handler.splitByWhitespace import process

@invocation(
  'jaid/invoke-node-text-util/splitByWhitespace',
  title='Split by Whitespace',
  tags=[
    'collection',
    'space',
    'split',
    'string',
    'strings',
    'text',
    'whitespace',
  ],
  category='string',
  version='1.0.0',
)
class SplitByWhitespaceInvocation(BaseInvocation):
  """Splits the given text on whitespace, returns a list of strings."""

  text: str = InputField(
    title='Text',
    description='Input text',
  )

  def invoke(self, context) -> StringCollectionOutput:
    output = process(self.text)
    return StringCollectionOutput(collection=output)
