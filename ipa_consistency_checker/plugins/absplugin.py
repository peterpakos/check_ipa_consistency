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
Abstract classes for checker plugins
"""
from __future__ import absolute_import
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class LDAPPlugin(object):
    """
    Abstract plugin class for checker
    """
    def __init__(self, ldap_conn, **options):
        self.conn = ldap_conn
        self.options = options

    @abc.abstractmethod
    def execute(self):
        """This is executed by workers, plugin implementation should be here
        :return: dict with results
        """
        return {}
