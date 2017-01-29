# Authors:
#   Martin Basti <mbasti@redhat.com>
#
# Copyright (C) 2016  Peter Pakos <peter.pakos@wandisco.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Module contains formatters of script output
"""

from __future__ import absolute_import
from __future__ import print_function

import abc
import sys
from pprint import pprint

import yaml
import six
from six import StringIO

from tabulate import tabulate

from .registry import FormatterRegistry, CheckerRegistry


@six.add_metaclass(abc.ABCMeta)
class Formatter(object):
    """
    Abstract class for a formatter
    """
    def __init__(self, **options):
        self.options = options

    @abc.abstractmethod
    def format_output(self, data):
        """Take dict representation of check results and convert them into
        text format
        :param data: dict
        :return: string
        """
        return repr(data)

    def print(self, data, stream=None):
        """Print formatted output to specified stream, STDOUT by default
        :param data: dict
        :param stream:
        """
        if stream is None:
            stream = sys.stdout
        output = self.format_output(data)
        print(output, file=stream)


@FormatterRegistry.register('python', description="Python repr() format")
class PythonFormatter(Formatter):
    """
    Print output in python repr format (can be imported back to python by
    copy and paste)
    """
    def format_output(self, data):
        output = StringIO()
        pprint(data, stream=output)
        return output.getvalue()


@FormatterRegistry.register('yaml', description="YAML format")
class YAMLFormatter(Formatter):
    """
    Print output in YAML format
    """
    def format_output(self, data):
        return yaml.dump(data)


@FormatterRegistry.register('table', description="Table format")
class TableFormatter(Formatter):
    """
    Print output in table
    """
    def format_output(self, data):
        plugins = tuple(CheckerRegistry.iter_names())
        servers = tuple(data.keys())
        header = ('Servers:',) + servers + ('STATUS',)
        table = []
        for name in plugins:
            line = [CheckerRegistry.get_description(name)]
            for server in servers:
                item = data[server].get(name, 'N/A')
                line.append(item)
            line.append('')  # status
            table.append(line)

        return tabulate(table, headers=header)
