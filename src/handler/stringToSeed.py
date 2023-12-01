import hashlib

def process(text: str) -> str:
  hash = hashlib.sha256(text.encode('utf-8')).digest()
  seed = int.from_bytes(hash[:4], 'big')
  return seed
