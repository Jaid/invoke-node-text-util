import unittest

from ...src.handler.sanitizeText import process

fixtures = [
  {
    'args': [
      "foo bar",
    ],
    'expected': "foo bar",
  },
  {
    'args': [
      "foo\nbar",
    ],
    'expected': "foo bar",
  },
  {
    'args': [
      "foo\n\nbar",
    ],
    'expected': "foo bar",
  }
]

class TestSanitizeText(unittest.TestCase):
  def test(self):
    for fixture in fixtures:
      self.assertEqual(process(*fixture['args']), fixture['expected'])

if __name__ == '__main__':
  unittest.main()
