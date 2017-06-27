import logging
import unittest

from randomload import log


class TestLog(unittest.TestCase):

    def test_default_log_level(self):
        """Test that the default log level is INFO."""
        self.assertEquals(log.logger.level, logging.INFO)
