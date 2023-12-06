import unittest

from src.handler import sanitizePrompt

fixtures = [
  {
    'args': {
      'text': "foo   bar",
      'commaOnLinebreak': True,
    },
    'expected': "foo bar",
  },
  {
    'args': {
      'text': "foo\nbar",
      'commaOnLinebreak': True,
    },
    'expected': "foo, bar",
  },
  {
    'args': {
      'text': "\t        f\n   \too   \r\n bar  ",
      'commaOnLinebreak': True,
    },
    'expected': "f, oo, bar",
  },
  {
    'args': {
      'text': "\t        f\n   \too   \r\n bar  ",
      'commaOnLinebreak': False,
    },
    'expected': "f oo bar",
  }
]

class TestSanitizePrompt(unittest.TestCase):
  def test(self):
    for fixture in fixtures:
      input = fixture['args']
      output = sanitizePrompt.process(**input)
      expected = fixture['expected']
      self.assertEqual(output, expected)

if __name__ == '__main__':
  unittest.main()
