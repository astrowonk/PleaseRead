import unittest
from PleaseRead import InlineStyles, get_default_rules


class TestInlineStyles(unittest.TestCase):

    def test_stripe(self):
        t = InlineStyles(rules_dict=get_default_rules())
        self.assertEqual(t.stripe_rule, ('odd', 'background: #f5f5f5;'))
