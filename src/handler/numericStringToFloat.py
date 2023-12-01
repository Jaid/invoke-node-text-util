def process(text: str) -> float:
  text = text.strip()
  if text.endswith('%'):
    formattedText = text[:-1].strip()
    number = float(formattedText) / 100
  else:
    number = float(text)
  return number
