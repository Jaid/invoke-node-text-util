import unittest

from src.handler import resolveTextTemplate

fixtures = [
  {
    'args': {
      'template': "foo {{a}}",
      'context': {
        'a': "bar",
      },
    },
    'expected': "foo bar",
  },
  {
    'args': {
      'template': "foo {{a | upper}}",
      'context': {
        'a': "bar",
      },
    },
    'expected': "foo BAR",
  },
]

class TestResolveTextTemplate(unittest.TestCase):
  def test(self):
    for fixture in fixtures:
      input = fixture['args']
      output = resolveTextTemplate.process(**input)
      expected = fixture['expected']
      self.assertEqual(output, expected)

if __name__ == '__main__':
  unittest.main()
