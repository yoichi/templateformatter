#!/usr/bin/env python
import unittest

from template_formatter import TemplateFormatter


class TestTemplateFormatter(unittest.TestCase):
    def test_utf8_to_file(self):
        formatter = TemplateFormatter(['t/key.yml'])
        formatter.substitute_to_file('t/utf8.py.template', 't/utf8_output.py')
        with open('t/utf8.py') as f:
            expected = f.read()
        with open('t/utf8_output.py') as f:
            result = f.read()
        self.assertEqual(result, expected)

    def test_cp932_to_file(self):
        formatter = TemplateFormatter(['t/key.yml'])
        formatter.substitute_to_file('t/cp932.py.template', 't/cp932_output.py')
        with open('t/cp932.py') as f:
            expected = f.read()
        with open('t/cp932_output.py') as f:
            result = f.read()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
