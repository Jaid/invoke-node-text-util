import unittest

from src.handler import sanitizeText

fixtures = [
  {
    'args': {
      'text': "foo   bar",
    },
    'expected': "foo bar",
  },
  {
    'args': {
      'text': "foo\nbar",
    },
    'expected': "foo\nbar",
  },
  {
    'args': {
      'text': "         f\noo\r\nbar  ",
    },
    'expected': "f\noo\nbar",
  }
]

class TestSanitizeText(unittest.TestCase):
  def test(self):
    for fixture in fixtures:
      input = fixture['args']
      output = sanitizeText.process(**input)
      expected = fixture['expected']
      self.assertEqual(output, expected)

if __name__ == '__main__':
  unittest.main()
