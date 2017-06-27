import os
import sys
import unittest

from randomload.args import parser
from randomload.log import logging


class TestArgs(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.stderr = sys.stderr
        self.devnull = open(os.devnull, 'w')
        sys.stderr = self.devnull

    def tearDown(self):
        logging.disable(logging.NOTSET)
        sys.stderr = self.stderr
        self.devnull.close()

    def test_config_file(self):
        """Tests the --config-file command line argument option."""
        l = []
        args = parser.parse_args(l)
        self.assertEquals(args.config_file, '/etc/randomload/randomload.yaml')

        l = ['--config-file', 'testfile.yaml']
        args = parser.parse_args(l)
        self.assertEquals(args.config_file, 'testfile.yaml')

    def test_action_set(self):
        """Tests the --action-set commaind line argument option."""
        l = []
        args = parser.parse_args(l)
        self.assertEquals(args.action_set, 'all')

        l = ['--action-set', 'read']
        args = parser.parse_args(l)
        self.assertEquals(args.action_set, 'read')

        l = ['--action-set', 'invalid']
        with self.assertRaises(SystemExit):
            args = parser.parse_args(l)

    def test_action(self):
        """Tests the --action command line argument option."""
        l = []
        args = parser.parse_args(l)
        self.assertFalse(args.action)

        l = ['--action', 'invalid_action']
        with self.assertRaises(SystemExit):
            args = parser.parse_args()

        l = ['--action', 'server_list', '--action', 'volume_list']
        args = parser.parse_args(l)
        expected_actions = ['server_list', 'volume_list']
        for i, ea in enumerate(expected_actions):
            self.assertEquals(ea, args.action[i])

    def test_debug(self):
        """Tests the --debug command line argument option."""
        l = []
        args = parser.parse_args(l)
        self.assertFalse(args.debug)

        l = ['--debug']
        args = parser.parse_args(l)
        self.assertTrue(args.debug)
