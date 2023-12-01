from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import FloatOutput

from ..handler.numericStringToFloat import process

@invocation(
  'jaid/invoke-node-text-util/numericStringToFloat',
  title='Numeric String to Float',
  tags=[
    'convert',
    'float',
    'normalize',
    'number',
    'percent',
    'percentage',
    'rescale',
    'scale',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class NumericStringToFloatInvocation(BaseInvocation):
  """Converts a string to a float. If the input ends with a percent sign, it will be rescaled accordingly."""
  text: str = InputField(
    title='Text',
    description='Input text',
  )

  def invoke(self, context) -> FloatOutput:
    output = process(self.text)
    return FloatOutput(value=output)
