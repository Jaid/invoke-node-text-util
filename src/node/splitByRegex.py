import re

from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringCollectionOutput

from ...src.handler.splitByRegex import process

@invocation(
  'jaid/invoke-node-text-util/splitByRegex',
  title='Split by RegEx',
  tags=[
    'collection',
    'regex',
    'regexp',
    'split',
    'string',
    'strings',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class SplitByRegexInvocation(BaseInvocation):
  """Splits the given text on every occurrence matched by a regular expression, returns a list of strings."""

  text: str = InputField(
    title='Text',
    description='Input text',
  )
  expression: str = InputField(
    title='Regular Expression',
    default='[,\\s]+',
    description='Regular expression for splitting',
  )

  def invoke(self, context) -> StringCollectionOutput:
    output = process(self.text, self.expression)
    return StringCollectionOutput(collection=output)
