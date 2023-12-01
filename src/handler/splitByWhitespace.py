import re

expression = re.compile(r'\s+')

def process(text: str) -> list[str]:
  text = text.strip()
  split = re.split(expression, text)
  return split
