def process(text: str, splitter: str) -> list[str]:
  text = text.strip()
  split = text.split(splitter)
  return split
