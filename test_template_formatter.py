#!/usr/bin/env python
import unittest

from template_formatter import TemplateFormatter


class TestTemplateFormatter(unittest.TestCase):
    def _test_same_content(self, path1, path2):
        with open(path1, 'rb') as f1:
            c1 = f1.read()
        with open(path2, 'rb') as f2:
            c2 = f2.read()
        self.assertEqual(c1, c2)

    def test_substitute_to_file(self):
        formatter = TemplateFormatter(['t/key.yml'])
        formatter.substitute_to_file('t/ascii.py.template',
                                     't/ascii_output.py')
        self._test_same_content('t/ascii.py',
                                't/ascii_output.py')

    def test_substitute_keyerror(self):
        formatter = TemplateFormatter([])
        with self.assertRaises(KeyError):
            formatter.substitute('t/ascii.py.template')

    def test_confusing(self):
        formatter = TemplateFormatter([])
        formatter.substitute_to_file('t/confusing.py.template',
                                     't/confusing_output.py')
        self._test_same_content('t/confusing.py.template',
                                't/confusing_output.py')
        import t.confusing_output as confusing
        self.assertEqual(confusing.CONFUSING, '${')

    def test_utf8_to_file(self):
        formatter = TemplateFormatter(['t/key.yml'])
        formatter.substitute_to_file('t/utf8.py.template',
                                     't/utf8_output.py')
        self._test_same_content('t/utf8.py',
                                't/utf8_output.py')

    def test_cp932_to_file(self):
        formatter = TemplateFormatter(['t/key.yml'])
        formatter.substitute_to_file('t/cp932.py.template',
                                     't/cp932_output.py')
        self._test_same_content('t/cp932.py',
                                't/cp932_output.py')


if __name__ == '__main__':
    unittest.main()
