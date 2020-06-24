#!/usr/bin/env python
from string import Template
import yaml


class TemplateFormatter(object):
    """Template Formatter.

    Format string by using template file and dictionary loaded from yaml files.
    """
    def __init__(self, yaml_list):
        """Load dictionary for substitution.

        Each yaml file is assumed to represent dictionary.
        If the same key appears in some input files, latter is used.

        :param list[str] yaml_list: list of yaml file path

        :attribute dict _format_dict: dictionary for substitution
        """
        self._format_dict = {}
        for path in yaml_list:
            with open(path) as f:
                data = yaml.safe_load(f)
                assert isinstance(data, dict)
                self._format_dict.update(data)

    def substitute(self, template_path):
        """Read template file and substitute.

        :param str template_path: template file path

        :return: formatted string
        :rtype: str
        """
        with open(template_path) as f:
            template = Template(f.read())
        return template.substitute(**self._format_dict)

    def substitute_to_file(self, template_path, output_path):
        """Read template file and write substituted string to a file.

        :param str template_path: template file path
        :param str output_path: output file path
        """
        with open(output_path, 'w') as of:
            of.write(self.substitute(template_path))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('usage: {0} template_path [yaml_path ...]'.format(sys.argv[0]))
        sys.exit(-1)
    template_path = sys.argv[1]
    yaml_list = sys.argv[2:]
    formatter = TemplateFormatter(yaml_list)
    print(formatter.substitute(template_path))
