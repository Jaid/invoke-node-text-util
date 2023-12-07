import jinja2

jinjaEnvironment = jinja2.Environment()

def process(template: str, context: dict) -> str:
  template = jinjaEnvironment.from_string(
    source=template,
  )
  text = template.render(context)
  return text
