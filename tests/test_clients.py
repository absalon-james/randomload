import mock
import unittest

from osc_lib.clientmanager import ClientManager
from randomload.clients import clients


class TestClients(unittest.TestCase):

    @mock.patch('randomload.clients.clientmanager.ClientManager.setup_auth')
    def test_call(self, m_setup_auth):
        """Test that calling clients() gets an instance of ClientManager"""
        self.assertTrue(isinstance(clients(), ClientManager))
