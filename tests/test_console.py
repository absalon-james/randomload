import unittest

from randomload.console import load_actions
from randomload.actions import ALL


class TestLoadActions(unittest.TestCase):

    def test_no_chosen_actions(self):
        """Test loading of an action set with no chosen_actions."""
        action_set = 'all'
        chosen_actions = []
        actions = load_actions(action_set, chosen_actions)
        for i, a in enumerate(ALL.values()):
            self.assertTrue(a in actions)

    def test_chosen_actions(self):
        """Test loading of an action set with a chosen_action."""
        action_set = 'all'
        chosen_actions = ['server_create']
        actions = load_actions(action_set, chosen_actions)
        self.assertEquals(len(actions), 1)
        self.assertEquals(ALL['server_create'], actions[0])


class TestRun(unittest.TestCase):
    pass
