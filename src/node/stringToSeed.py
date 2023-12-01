import hashlib

from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import IntegerOutput

from ..handler.stringToSeed import process

@invocation(
  'jaid/invoke-node-text-util/stringToSeed',
  title='String to Seed',
  tags=[
    'convert'
    'seed'
    'random',
  ],
  category='string',
  version='1.0.0',
)
class StringToSeedInvocation(BaseInvocation):
  """Converts any string to a 32-bit uint seed (0-4294967295)"""

  text: str = InputField(
    title='Text',
    description='Input text',
  )

  def invoke(self, context) -> IntegerOutput:
    output = process(self.text)
    return IntegerOutput(value=output)
