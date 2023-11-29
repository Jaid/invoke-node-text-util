from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringCollectionOutput

def process(text: str, splitter: str) -> list[str]:
  text = text.strip()
  split = text.split(splitter)
  return split

@invocation(
  'jaid/invoke-node-text-util/split',
  title='Split String',
  tags=[
    'collection',
    'split',
    'string',
    'strings',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class SplitInvocation(BaseInvocation):
  """Splits the given text on every occurrence of the specified splitter."""
  text: str = InputField(
    title='Text',
    description='Input text',
  )
  splitter: str = InputField(
    title='Splitter',
    default=',',
    description="Search string for splitting",
  )

  def invoke(self, context) -> StringCollectionOutput:
    output = process(self.text, self.splitter)
    return StringCollectionOutput(collection=output)
