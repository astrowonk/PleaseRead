import unittest
from PleaseRead import Message


class TestMessage(unittest.TestCase):

    def test_add(self):
        m = Message()
        m.add_text("## Hello")

        m2 = Message()
        m2.add_text("## Good Bye")

        new = m + m2
        self.assertEqual(len(new.body_list), 2)
        self.assertCountEqual(['## Hello', '## Good Bye'], new.body_list)
