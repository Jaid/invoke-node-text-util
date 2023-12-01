import re

def process(text: str, expression: str) -> list[str]:
  text = text.strip()
  split = re.split(expression, text)
  return split
