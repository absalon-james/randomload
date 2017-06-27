import unittest

from randomload import utils


class TestRandomName(unittest.TestCase):

    def test_defaults(self):
        """Test default behaviour."""
        name = utils.randomname()

        # Should start with random-
        self.assertTrue(name.startswith('random-'))

        # Should contain 'random-' + 6 random characters.
        self.assertEquals(len(name), 13)

    def test_prefix(self):
        """Test optional prefix."""
        prefix = 'test'
        name = utils.randomname(prefix=prefix)
        # Should start with 'test-'
        self.assertTrue(name.startswith(prefix + '-'))
        # should contain 'test-' + 6 random characters.
        self.assertEquals(len(name), 11)

    def test_length(self):
        """Test optional length of random characters."""
        name = utils.randomname(l=0)
        self.assertEquals(len(name), 7)
        name = utils.randomname(l=2)
        self.assertEquals(len(name), 9)
