is_cssutils_available = False
try:
    import cssutils
    is_cssutils_available = True
except ImportError:
    pass

from bs4 import BeautifulSoup


class InlineStyles:
    """Create a class to convert CSS to inline styles.

    Parameters
    ----------
    css_string : str
        A string containing valid CSS. It'll be parsed with cssutils.parsestring
    """
    rule_dict = None

    def __init__(self, css_string: str = None, rules_dict: dict | None = None):
        if css_string:
            assert is_cssutils_available, "Optional install cssutils requried for parsing CSS string."
            self.css_rules = list(
                cssutils.parseString(css_string).cssRules.rulesOfType(
                    cssutils.css.CSSRule.STYLE_RULE))
            self.make_full_dictionary()
        elif rules_dict:
            self.rule_dict = rules_dict

    @staticmethod
    def smart_update(dict1: dict, dict2: dict):
        """Use regular dict1.update(dict2) unless the key exists, then add the strings.

        Parameters
        ----------
        dict1 : dict
            a dictionary
        dict2 : dict
            a dictionary to update dict1
        """
        if not any(x in dict1 for x in dict2.keys()):
            dict1.update(dict2)
            return
        for key, val in dict2.items():
            if key in dict1:
                dict1[key] = dict1[key] + val

    def make_full_dictionary(self):
        """Loop through all css_rules and create a dictionary mapping each element (e.g. td or th or p) to the style string for that element.
        """
        self.rule_dict = {}
        for rule in self.css_rules:
            new_rule = self.make_dict_for_rule(rule)
            self.smart_update(self.rule_dict, new_rule)

    @staticmethod
    def stripe_table(soup: BeautifulSoup):
        """Find tables in Beautfiul soup HTML and manually stripe the even rows like jupyter notebook styling. 
        This is done because nth-child rules can't be applied inline.

        Parameters
        ----------
        soup : BeautifulSoup
            An instance of BeautifulSoup
        """
        for table in soup.find_all('tbody'):
            for i, tr in enumerate(table.find_all('tr')):
                if i % 2 == 1:
                    tr['style'] += ' background: #f5f5f5;'

    def apply_rules_to_html(self, html: str) -> str:
        """Use the class to turn HTML into inline styled HTML

        Parameters
        ----------
        html : str
            A string that contains HTML. It will be parsed with BeautifulSoup

        Returns
        -------
        str
            HTML containing inline styles.
        """
        soup = BeautifulSoup(html, 'html.parser')
        for elem in self.rule_dict.keys():
            for item in soup.find_all(elem):
                item['style'] = self.rule_dict.get(elem)
        self.stripe_table(soup)
        return str(soup)

    @staticmethod
    def make_dict_for_rule(rule: cssutils.css.CSSRule) -> dict:
        """For a single CSSrule, create a dict of tags to style text.

        Parameters
        ----------
        rule : cssutils.css.CSSRule
            A single CSSrule from cssutils

        Returns
        -------
        dict
            A dictionary like {'tr': 'text-align: right;'}
        """
        return {
            x.selectorText: rule.style.cssText.replace('\n', ' ') + ';'
            for x in rule.selectorList
        }
