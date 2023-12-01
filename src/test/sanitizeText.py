import unittest

from src.handler import sanitizeText

fixtures = [
  {
    'args': {
      'text': "foo bar",
    },
    'expected': "foo bar",
  },
  {
    'args': {
      'text': "foo\nbar",
    },
    'expected': "foo bar",
  },
  # {
  #   'args': {
  #     'text': "         f\noo\r\nbar  ",
  #   },
  #   'expected': "f\noo bar",
  # }
]

class TestSanitizeText(unittest.TestCase):
  def test(self):
    for fixture in fixtures:
      self.assertEqual(sanitizeText.process(**fixture['args']), fixture['expected'])

if __name__ == '__main__':
  unittest.main()
