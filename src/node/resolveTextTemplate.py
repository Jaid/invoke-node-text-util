from invokeai.app.invocations.baseinvocation import (
  BaseInvocation,
  InputField,
  invocation,
)
from invokeai.app.invocations.primitives import StringOutput

from ..handler.resolveTextTemplate import process

@invocation(
  'jaid/invoke-node-text-util/resolveTextTemplate',
  title='Resolve Text Template',
  tags=[
    'dynamic',
    'format'
    'jinja',
    'jinja2',
    'replace',
    'resolve',
    'string',
    'strings',
    'template',
    'templating',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class ResolveTextTemplateInvocation(BaseInvocation):
  """Dynamically replaces placeholders in a text template with values from the given input context using Jinja2"""

  text: str = InputField(
    title='Template',
    description='Template code with Jinja2 syntax',
    ui_order=5
  )

  contextA: str = InputField(
    title='a',
    description='Value for placeholder {{a}}',
  )

  def createContext(self) -> dict:
    context = {}
    context['a'] = self.contextA
    return context

  def invoke(self, context) -> StringOutput:
    userContext = self.createContext()
    output = process(self.text, userContext)
    return StringOutput(value=output)

@invocation(
  'jaid/invoke-node-text-util/resolveTextTemplateDoubleInput',
  title='Resolve Text Template (2 Inputs)',
  tags=[
    'dynamic',
    'format'
    'jinja',
    'jinja2',
    'replace',
    'resolve',
    'string',
    'strings',
    'template',
    'templating',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class ResolveTextTemplateDoubleInputInvocation(ResolveTextTemplateInvocation):
  """Dynamically replaces placeholders in a text template with values from the given inputs (up to 2) context using Jinja2"""

  contextB: str = InputField(
    title='b',
    description='Value for placeholder {{b}}',
  )

  def createContext(self) -> dict:
    context = super().createContext()
    context['b'] = self.contextB
    return context

@invocation(
  'jaid/invoke-node-text-util/resolveTextTemplateTripleInput',
  title='Resolve Text Template (3 Inputs)',
  tags=[
    'dynamic',
    'format'
    'jinja',
    'jinja2',
    'replace',
    'resolve',
    'string',
    'strings',
    'template',
    'templating',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class ResolveTextTemplateTripleInputInvocation(ResolveTextTemplateDoubleInputInvocation):
  """Dynamically replaces placeholders in a text template with values from the given inputs (up to 3) context using Jinja2"""

  contextC: str = InputField(
    title='c',
    description='Value for placeholder {{c}}',
  )

  def createContext(self) -> dict:
    context = super().createContext()
    context['c'] = self.contextC
    return context

@invocation(
  'jaid/invoke-node-text-util/resolveTextTemplateQuadrupleInput',
  title='Resolve Text Template (4 Inputs)',
  tags=[
    'dynamic',
    'format'
    'jinja',
    'jinja2',
    'replace',
    'resolve',
    'string',
    'strings',
    'template',
    'templating',
    'text',
  ],
  category='string',
  version='1.0.0',
)
class ResolveTextTemplateQuadrupleInputInvocation(ResolveTextTemplateTripleInputInvocation):
  """Dynamically replaces placeholders in a text template with values from the given inputs (up to 4) context using Jinja2"""

  contextD: str = InputField(
    title='d',
    description='Value for placeholder {{d}}',
  )

  def createContext(self) -> dict:
    context = super().createContext()
    context['d'] = self.contextD
    return context
